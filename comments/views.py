import json

from django.views           import View
from django.core.exceptions import ValidationError
from django.http            import JsonResponse

from core.validations       import validate_content
from core.utils             import authorization
from posts.models           import Post
from comments.models        import Comment

class CommentView(View):
    @authorization
    def post(self, request):
        try:
            user = request.user
            data = json.loads(request.body)

            content = data['content']
            post_id = data['post_id']

            validate_content(content, 1, 1500)

            post = Post.objects.get(id=post_id)

            Comment.objects.create(post=post, user=user, content=content)

            return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'BODY_REQUIRED'}, status=400)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'MESSAGE': e.message}, status=400)

        except ValueError:
            return JsonResponse({'MESSAGE': 'INVALID_POST_ID'}, status=400)

        except Post.DoesNotExist:
            return JsonResponse({'MESSAGE': 'POST_NOT_FOUND'}, status=400)

    @authorization
    def delete(self, request):
        comment_id = request.GET.get('comment_id')
        user       = request.user
        try:
            if not comment_id:
                return JsonResponse({'MESSAGE': 'COMMENT_ID_REQUIRED'}, status=400)

            comment = Comment.objects.get(id=comment_id)

            if comment.user_id != user.id:
                return JsonResponse({'MESSAGE': 'AUTHENTICATION_ERROR'}, status=401)

            comment.delete()
            return JsonResponse({'MESSAGE': 'COMMENT_DELETE_SUCCESS'}, status=200)

        except ValueError:
            return JsonResponse({'MESSAGE': 'INVALID_COMMENT_ID'}, status=400)

        except Comment.DoesNotExist:
            return JsonResponse({'MESSAGE': 'COMMENT_NOT_FOUND'}, status=400)

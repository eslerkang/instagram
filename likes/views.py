import json

from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.views           import View

from likes.models           import Like
from posts.models           import Post
from core.utils             import authorization


class LikeView(View):
    @authorization
    def post(self, request):
        try:
            data    = json.loads(request.body)
            user    = request.user

            post_id = data['post_id']
            post    = Post.objects.get(id=post_id)

            like    = Like.objects.get_or_create(user=user, post=post)

            if not like[1]:
                like[0].delete()
                return JsonResponse({'MESSAGE': 'LIKE_CANCEL_SUCCESS'}, status=200)

            return JsonResponse({'MESSAGE': 'LIKED_SUCCESS'}, status=200)

        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'BODY_REQUIRED'}, status=400)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'MESSAGE': 'INVALID_POST_ID'}, status=400)

        except Post.DoesNotExist:
            return JsonResponse({'MESSAGE': 'POST_NOT_FOUND'}, status=400)

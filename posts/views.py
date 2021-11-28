import json

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError
from django.db.models       import F

from core.validations import validate_url, validate_content
from core.utils       import authorization
from posts.models     import Post, Image

class PostView(View):
    @authorization
    def post(self, request):
        try:
            data    = json.loads(request.body)
            user    = request.user
            images  = data['images']
            content = data['content']

            if type(images) is not list:
                return JsonResponse({'MESSAGE': 'IMAGES_MUST_BE_LIST'}, status=400)

            if type(content) is not str:
                return JsonResponse({'MESSAGE': 'CONTENT_MUST_BE_STR'}, status=400)

            if len(images) < 1:
                return JsonResponse({'MESSAGE': 'IMAGE_REQUIRED'}, status=400)

            validate_content(content, 0, 1500)

            post       = Post(user=user, content=content)
            image_list = []

            for image in images:
                validate_url(image)
                image_list.append(Image(url=image, post=post))

            post.save()
            Image.objects.bulk_create(image_list)

            return JsonResponse({'MESSAGE': 'CREATED'}, status=201)

        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'BODY_REQUIRED'}, status=400)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KEY_ERROR'}, status=400)

        except ValidationError as e:
            return JsonResponse({'MESSAGE': e.message}, status=400)

    def get(self, request):
        results = []
        posts   = Post.objects.prefetch_related(
            'image_set', 'comment_set'
        ).annotate(
            user_name=F('user__name')
        )

        for post, post_query in zip(
                posts.values('content', 'created_at', 'user_name'),
                posts
        ):
            post['images']   = list(post_query.image_set.values('url'))
            post['comments'] = list(post_query.comment_set.annotate(
                user_name=F('user__name')
            ).values('user_name', 'content'))
            results.append(post)

        return JsonResponse({'MESSAGE': results}, status=200)


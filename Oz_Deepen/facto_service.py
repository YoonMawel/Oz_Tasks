# 업로드 서비스 - 저장, 썸네일, 메타데이터, URL 생성
# AWS, 로컬, Streaming Pro 중 방식은 공장이 알아서
# save(file), create_thumbnail(file), extract(file), build(file) 메서드가 중요

from abc import ABC, abstractmethod
from http.client import UnknownProtocol


# ======================================================
# Product Interfaces
# ======================================================

class Storage(ABC):
    # ABC를 상속한 추상 클래스, 그리고 추상 팩토리 패턴 역할 기준 추상 제품(Abstract Product)
    # 역할 - 각 기능의 추상 제품 인터페이스(규칙)
    # 파일 저장의 공통 규칙(인터페이스) 정의
    # 실제 저장 x, "이런 메서드가 반드시 있어야 한다." 라고 선언만
    @abstractmethod
    def save(self, file): # file 이라는 파라미터 정의
        pass


class ThumbnailProcessor(ABC):
    # 썸네일 생성 공통 인터페이스
    # 추상 클래스, 추상 제품, 인터페이스
    # 구현체는 아무거나 상관 x
    # create_thumbnail(file) 메서드를 반드시 구현해야 함 (상속시)
    @abstractmethod
    def create_thumbnail(self, file):
        pass


class MetadataExtractor(ABC):
    # 메타데이터 추출 공통 규칙
    # 구현체 상관없이 extract(file) 메서드 제공
    @abstractmethod
    def extract(self, file):
        pass


class URLBuilder(ABC):
    # url 생성 공통 인터페이스
    # build(file) 메서드 제공
    @abstractmethod
    def build(self, file):
        pass


# ======================================================
# Enterprise (AWS 기반)
# ======================================================

class S3Storage(Storage):
    # Storage 인터페이스의 실제 구현체(구체 클래스)
    # Enterprise는 S3에 저장을 하겠다는 설정을 반영함
    # Storage를 상속하여 save()를 구현, 추상 클래스 규약을 따름
    def save(self, file):
        print("Saving file to S3")


class LambdaThumbnailProcessor(ThumbnailProcessor):
    # 썸네일 생성 구현체 (Enterprise 버전)
    # AWS Lambda 기반 처리라고 가정한 클래스
    def create_thumbnail(self, file):
        print("Generating thumbnail via AWS Lambda")


class MediaConvertMetadataExtractor(MetadataExtractor):
    # 메타데이터 추출 구현체 (Enterprise 버전)
    # AWS MediaConvert를 사용한다고 가정
    def extract(self, file):
        print("Extracting metadata via AWS MediaConvert")


class CloudFrontURLBuilder(URLBuilder):
    # URL 생성 구현체 (Enterprise 버전)
    # CloudFront Signed URL 생성 담당
    def build(self, file):
        print("Building CloudFront signed URL")


# ======================================================
# Startup (로컬 기반) 실제 구현 클래스
# ======================================================

class LocalStorage(Storage):
    # Startup 고객용 저장소 구현체
    # 로컬 디스크 저장이라고 가정함
    def save(self, file):
        print("Saving file to local storage")


class PillowThumbnailProcessor(ThumbnailProcessor):
    # Startup 고객용 썸네일 처리 구현체
    # Pillow 라이브러리 기반이라고 가정
    def create_thumbnail(self, file):
        print("Generating thumbnail via Pillow")


class FFmpegMetadataExtractor(MetadataExtractor):
    # Startup 고객용 메타데이터 추출 구현체
    # FFmpeg 기반이라고 가정
    def extract(self, file):
        print("Extracting metadata via FFmpeg")


class StaticURLBuilder(URLBuilder):
    # Startup 고객용 URL 생성 구현체
    # 정적 url 생성 담당
    def build(self, file):
        print("Building static URL")

# ====
# Privacy 고객 (보안이 중요함) 실제 구현 클래스 (이것도 추가)
# ====

# privacy_service = UploadService(privacy_factory) 실행시
# 생성자 호출을 위해 여기서 구현체 생성됨

class PrivateObjectStorage(Storage):
    # Privacy 고객용 저장소 구현체
    # 외부 공개 스토리지가 아닌 private object storage 사용
    def save(self, file):
        print("파일을 private object strage에 저장합니다.")


class InternalThumbnailProcessor(ThumbnailProcessor):
    # Privacy 고객용 썸네일 생성 구현체
    # 내부 폐쇄망 처리 서버에서 썸네일 생성
    def create_thumbnail(self, file):
        print("내부 폐쇄망 처리 서버에서 썸네일을 생성합니다.")


class InternalMetadataExtractor(MetadataExtractor):
    # Privacy 고객용 메타데이터 추출 구현체
    # 내부 분석 서비스 사용
    def extract(self, file):
        print("내부 분석 서비스에서 메타데이터를 추출합니다.")


class TokenTemporaryURLBuilder(URLBuilder):
    # Privacy 고객용 URL 생성 구현체
    # 토큰 기반 임시 URL 생성
    def build(self, file):
        print("토큰 기반 임시 URL을 생성합니다.")

# =====================================================
# Streaming Pro (추가)
# =====================================================

class CDNOriginStorage(Storage):
    # Streaming Pro 고객용 저장소 구현체
    # cdn 원본 저장소에 저장한다고 가정
    def save(self, file):
        print("파일을 cdn 스토리지에 저장합니다.")

class FrameCaptureThumbnailProcessor(ThumbnailProcessor):
    # 동영상 프레임 캡처 기반 썸네일 생성 담당
    def create_thumbnail(self, file):
        print("동영상에서 프레임을 캡처하여 썸네일을 생성합니다.")

class StreamingMediaAnalyzer(MetadataExtractor):
    # 스트리밍용 메타데이터 분석 담당
    def extract(self, file):
        print("스트리밍용 메타데이터를 분석합니다.")

class SignedStreamingURLBuilder(URLBuilder):
    # HLS/DASH 등 스트리밍용 서명 URL 생성 담당
    def build(self, file):
        print("서명 url을 생성합니다.")


# ======================================================
# Abstract Factory (추상 팩토리)
# ======================================================

# 고객사별 기능 4종을 세트로 만들어줌
# 공장이라면 이 4가지 기능은 만들 수 있어야 함

class MediaInfrastructureFactory(ABC):
    # 추상 클래스(ABC)
    # ** 추상 팩토리 (Abstract Factory) **
    @abstractmethod
    def create_storage(self) -> Storage: #추상 메서드
        pass

    @abstractmethod
    def create_thumbnail_processor(self) -> ThumbnailProcessor: #추상 메서드
        pass

    @abstractmethod
    def create_metadata_extractor(self) -> MetadataExtractor: #추상 메서드
        pass

    @abstractmethod
    def create_url_builder(self) -> URLBuilder: #추상 메서드
        pass


# ======================================================
# Concrete Factories (구체 팩토리)
# ======================================================

class EnterpriseMediaFactory(MediaInfrastructureFactory):
    # Enterprise 고객사 전용 공장
    # AWS 계열 부품 4개를 한 세트로 만들어줌
    # LocalStorage같은 타 고객사 부품을 섞지 않음으로써 인프라 혼합 방지

    def create_storage(self):
        return S3Storage()

    def create_thumbnail_processor(self):
        return LambdaThumbnailProcessor()

    def create_metadata_extractor(self):
        return MediaConvertMetadataExtractor()

    def create_url_builder(self):
        return CloudFrontURLBuilder()


class StartupMediaFactory(MediaInfrastructureFactory):
    # Startup 고객사 전용 구체 팩토리 (전용 공장)
    # 로컬,Pillow,FFmpeg,static URL을 세트로 제공

    def create_storage(self):
        return LocalStorage()

    def create_thumbnail_processor(self):
        return PillowThumbnailProcessor()

    def create_metadata_extractor(self):
        return FFmpegMetadataExtractor()

    def create_url_builder(self):
        return StaticURLBuilder()

# === 추가 ===

class PrivacyMediaFactory(MediaInfrastructureFactory):
    #privacy concrete factory 보안 중시 고객 전용 구체 팩토리
    # 메인 실행부에서 특정 서비스 실행시 구체 팩토리 (해당 구역)으로 넘어옴
    # 그래서 해당 클래스의 인스턴스를 아래와 같이 생성함 (구체 팩토리 생성)

    def create_storage(self):
        return PrivateObjectStorage()

    def create_thumbnail_processor(self):
        return InternalThumbnailProcessor()

    def create_metadata_extractor(self):
        return InternalMetadataExtractor()

    def create_url_builder(self):
        return TokenTemporaryURLBuilder()

# ===
# 추가 - Streaming Pro 전용 팩토리
# ===

class StreamingProMediaFactory(MediaInfrastructureFactory):

    def create_storage(self):
        return CDNOriginStorage()

    def create_thumbnail_processor(self):
        return FrameCaptureThumbnailProcessor()

    def create_metadata_extractor(self):
        return StreamingMediaAnalyzer()

    def create_url_builder(self):
        return SignedStreamingURLBuilder()


# ======================================================
# Client (업로드 서비스)
# ======================================================

class UploadService:
    def __init__(self, factory: MediaInfrastructureFactory):
        # 특정 업로드 서비스 시작 시 팩토리에서 필요한 기능을 받아옴
        # 직접적으로 특정 인프라를 명시하지 않음 (ex. S3storage)
        self.storage = factory.create_storage() #여기서 전부 각각 해당 서비스의 구체 팩토리로 반환됨
        self.thumbnail = factory.create_thumbnail_processor() #썸네일 구체 팩토리로 반환
        self.metadata = factory.create_metadata_extractor() #메타데이터 추출 구체 팩토리로 반환
        self.url_builder = factory.create_url_builder() # url 생성 구체 팩토리로 반환

        #예를 들어 factory.create_storage() -> PrivateObjectStorage() 로 반환 되는 것

    def upload(self, file):
        # 하단 메인 실행부에서 privacy_service.upload("privacy_video.mp4") 부분의 흐름
        # 그래서 각자 반환된 객체들이 해당 함수를 통해 호출되고, 출력됨
        # 공통 인터페이스 메서드만 호출 -> 특정 인프라를 알 수 없음
        print("\n=== Upload Start ===")
        self.storage.save(file) # 저장
        self.thumbnail.create_thumbnail(file) # 썸네일 생성
        self.metadata.extract(file) # 메타데이터 추출
        self.url_builder.build(file) # URL 생성
        print("=== Upload Complete ===\n")


# ======================================================
# 실행 예시
# ======================================================

# 1. 메인 실행부 - 어느 고객사로 할지 결정
# ex. privacy 선택시 privacy 고객용 구체 팩토리 객체 생성
if __name__ == "__main__":

    enterprise_factory = EnterpriseMediaFactory()
    enterprise_service = UploadService(enterprise_factory)
    enterprise_service.upload("enterprise_video.mp4")

    startup_factory = StartupMediaFactory()
    startup_service = UploadService(startup_factory)
    startup_service.upload("startup_image.png")

    # privacy 추가
    privacy_factory = PrivacyMediaFactory() # Privacy 고객용 구체 팩토리 객체 생성 (위에 코드 있음)
    privacy_service = UploadService(privacy_factory) # UploadService에 팩토리를 전달
    privacy_service.upload("privacy_video.mp4") # UploadService에서 생성자 반환 후 업로드 실행

    # streaming pro 실행 부분 추가
    streaming_factory = StreamingProMediaFactory()
    streaming_service = UploadService(streaming_factory)
    streaming_service.upload("streaming_movie.m3u8")
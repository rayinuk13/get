class Get < Formula
  desc "Dead-simple terminal tool to download YouTube videos and audio"
  homepage "https://github.com/rayinuk13/get"
  url "https://github.com/rayinuk13/get/archive/refs/tags/v1.0.0.tar.gz"
  version "1.0.0"
  license "MIT"

  depends_on "ffmpeg"
  depends_on "yt-dlp"

  def install
    bin.install "get.py" => "get"
  end

  test do
    assert_match "get v1.0.0", shell_output("#{bin}/get --help")
  end
end

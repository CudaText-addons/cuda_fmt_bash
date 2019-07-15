Formatter for Bash script, using Beautysh library.

Quote from Beautysh readme:
  This program takes upon itself the hard task of beautifying Bash scripts
  (yeesh). Processing Bash scripts is not trivial, they aren't like C or Java
  programs — they have a lot of ambiguous syntax, and (shudder) you can use
  keywords as variables. Years ago, while testing the first version of this
  program, I encountered this example:

  done=0;while (( $done <= 10 ));do echo done=$done;done=$((done+1));done

  Same name, but three distinct meanings (sigh). The Bash interpreter can sort out
  this perversity, but I decided not to try to recreate the Bash interpreter to
  beautify a script. This means there will be some border cases this Python
  program won't be able to process. But in tests with large Linux system
  Bash scripts, its error-free score was ~99%.

Formatter has config file with Beautysh options.

Author: Alexey Torgashin (CudaText)
License: MIT

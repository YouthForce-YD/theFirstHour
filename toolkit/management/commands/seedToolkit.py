from django.core.management.base import BaseCommand
from toolkit.models import Situation, EvidenceStep, SupportChannel


class Command(BaseCommand):
    def handle(self, *args, **options):
        situationsData = [
            {
                'slug': 'harassment-and-threats',
                'titleBn': 'হয়রানি ও হুমকি',
                'titleEn': 'Harassment & threats',
                'iconName': 'message-square-warning',
                'immediateActionBn': 'ইনবক্স বা কমেন্টে কুরুচিপূর্ণ বার্তা, ভয়ভীতি বা শারীরিক ক্ষতির হুমকি পেলে পাল্টা উত্তর দেবেন না। প্রথমেই তারিখ, সময় ও প্রেরকের ইউজারনেমসহ সম্পূর্ণ কথোপকথনের স্ক্রিনশট নিন।',
                'immediateActionEn': 'Do not engage or reply to abusive messages or physical threats. Immediately capture screenshots showing the sender\'s username, timestamps, and full message thread.',
                'detailedStepsBn': 'হুমকিদাতার মেসেজ বা কমেন্টের স্ক্রিনশট নিন যেখানে তারিখ, সময় এবং ইউজারনেম স্পষ্ট দেখা যায়।\nহুমকিদাতার প্রোফাইলের স্থায়ী লিংক (URL) এবং পোস্টের লিংক কপি করে নোটপ্যাডে বা আমাদের ভল্টে সংরক্ষণ করুন।\nপ্রমাণ সংরক্ষণ শেষ হলে অ্যাকাউন্টটি মিউট বা ব্লক করুন এবং প্রাইভেসি সেটিংস "Friends Only" বা "Locked" করুন।\nশারীরিক ক্ষতির আশঙ্কা থাকলে তাৎক্ষণিকভাবে ৯৯৯ বা পুলিশ সাইবার সাপোর্টে (01320000888) যোগাযোগ করুন।',
                'detailedStepsEn': 'Capture full screenshots of the threatening messages or comments with visible date, time, and username.\nCopy the offender\'s permanent profile URL and message link into a safe note or your personal vault.\nOnce all evidence is preserved, block or restrict the account and lock your profile privacy settings.\nIf there is any threat of physical harm, call 999 or contact Police Cyber Support (01320000888) immediately.',
                'whatNotToDoBn': 'রাগের মাথায় পাল্টা হুমকি দেবেন না বা চ্যাট হিস্ট্রি ডিলিট করবেন না। প্রমাণ না রেখে ব্লক করলে পরে আইনি সহায়তা নেওয়া কঠিন হতে পারে।',
                'whatNotToDoEn': 'Do not reply with counter-threats or delete the conversation history. Blocking before saving URLs and screenshots may erase crucial digital evidence.',
                'platformGuideBn': 'ফেসবুক বা মেসেঞ্জারে মেসেজটির পাশে ট্যাপ করে "Report" -> "Harassment" বা "Violence and physical harm" অপশনটি বেছে নিয়ে সাবমিট করুন।',
                'platformGuideEn': 'Tap next to the message on Facebook or Messenger, select "Report", and choose "Harassment" or "Violence and physical harm".',
                'actionBtnBn': 'রিপোর্ট করুন',
                'actionBtnEn': 'Report Now',
                'displayOrder': 1,
            },
            {
                'slug': 'blackmail-and-sextortion',
                'titleBn': 'ব্ল্যাকমেইল ও সেক্সটরশন',
                'titleEn': 'Blackmail & sextortion',
                'iconName': 'lock-keyhole',
                'immediateActionBn': 'টাকা বা নতুন কোনো ছবি/ভিডিও দাবি করলে কখনোই তা দেবেন না। চ্যাট বা মেসেজ ডিলিট না করে সব প্রমাণ সংরক্ষণ করুন এবং দ্রুত পুলিশ সাইবার সাপোর্ট (PCSW) বা ৯৯৯-এ যোগাযোগ করুন।',
                'immediateActionEn': 'Never pay money or send more images/videos in response to demands. Keep all chat logs intact, preserve profile links, and immediately contact PCSW or 999.',
                'detailedStepsBn': 'ব্ল্যাকমেইলারের সাথে সব ধরনের যোগাযোগ ও কথোপকথন বন্ধ করুন, কিন্তু চ্যাট থ্রেড ডিলিট করবেন না।\nযেখানে টাকা বা ব্যক্তিগত ছবি দাবি করা হয়েছে, সেই মেসেজগুলোর স্ক্রিনশট এবং ব্যবহৃত বিকাশ/নগদ নম্বর বা প্রোফাইল লিংক সংরক্ষণ করুন।\nআপনার সোশ্যাল মিডিয়ার ফ্রেন্ডলিস্ট ও প্রোফাইল দ্রুত "Only Me" বা লক করে দিন যাতে অপরাধী আপনার পরিচিতদের খুঁজে না পায়।\nবিলম্ব না করে PCSW (01320000888) অথবা জাতীয় হেল্পলাইন ১০৯-এ যোগাযোগ করে আইনি সহায়তা নিন।',
                'detailedStepsEn': 'Stop replying to the blackmailer immediately, but do not delete the chat thread.\nTake screenshots of the extortion demands, payment numbers, and the offender\'s profile URL.\nSet your social media friend list and profile to "Only Me" or locked so the offender cannot target your contacts.\nContact Police Cyber Support for Women (01320000888) or National Helpline 109 right away.',
                'whatNotToDoBn': 'কখনোই টাকা পাঠাবেন না বা নতুন কোনো ছবি/ভিডিও দেবেন না। টাকা দিলে ব্ল্যাকমেইলারের দাবি বন্ধ হয় না বরং আরও বাড়ে।',
                'whatNotToDoEn': 'Never pay money or send additional intimate photos. Paying does not stop extortion; it signals that they can demand more.',
                'platformGuideBn': 'StopNCII.org ওয়েবসাইটে আপনার ছবির ডিজিটাল হ্যাশ তৈরি করে জমা দিতে পারেন, যাতে ফেসবুক ও ইনস্টাগ্রামে ছবিটি কেউ আপলোড করতে না পারে।',
                'platformGuideEn': 'You can generate a secure digital hash of intimate images at StopNCII.org to block them from being uploaded across Facebook and Instagram.',
                'actionBtnBn': 'জরুরি সহায়তা নিন',
                'actionBtnEn': 'Emergency Help',
                'displayOrder': 2,
            },
            {
                'slug': 'image-video-leaks-and-deepfakes',
                'titleBn': 'ছবি/ভিডিও ছড়ানো বা ডিপফেক',
                'titleEn': 'Image/video leaks & deepfakes',
                'iconName': 'image-off',
                'immediateActionBn': 'অনুমতি ছাড়া ব্যক্তিগত ছবি/ভিডিও বা এআই ডিপফেক ছড়ানো হলে পোস্টের ইউআরএল (URL) ও প্রোফাইল লিংক কপি করে রাখুন। প্ল্যাটফর্মে রিপোর্ট করার পাশাপাশি সাইবার সাপোর্টে জানান।',
                'immediateActionEn': 'Save the exact post URLs, uploader profile links, and dated screenshots before reporting the content on the platform and reaching out to cyber support.',
                'detailedStepsBn': 'যে পেজ, গ্রুপ বা আইডি থেকে ছবি/ভিডিও পোস্ট করা হয়েছে, তার সুনির্দিষ্ট পোস্ট লিংক (URL) ও প্রোফাইল লিংক কপি করে রাখুন।\nপোস্টের তারিখ, সময় এবং আপলোডকারীর নামসহ স্ক্রিনশট নিন।\nপ্ল্যাটফর্মের "Non-consensual intimate images" ক্যাটাগরিতে সরাসরি রিপোর্ট করুন।\nদ্রুত কনটেন্ট টেকডাউন (মুছে ফেলা) করার জন্য PCSW (01320000888)-এ প্রমাণগুলো পাঠান।',
                'detailedStepsEn': 'Copy the exact post URL and the uploader\'s profile link where the image, video, or deepfake was shared.\nTake dated screenshots showing the uploader\'s account details and post timestamp.\nReport the post directly on the platform under "Non-consensual intimate images" or abusive content.\nSubmit the URLs and screenshots to PCSW (01320000888) for official takedown assistance.',
                'whatNotToDoBn': 'পোস্টের কমেন্ট বক্সে গিয়ে তর্ক করবেন না; এতে পোস্টটির রিচ (Reach) বা অ্যালগরিদম ভিউ আরও বেড়ে যেতে পারে।',
                'whatNotToDoEn': 'Avoid commenting publicly on the leaked post, as engagement can increase its algorithmic reach before takedown.',
                'platformGuideBn': 'ফেসবুক বা ইনস্টাগ্রামে পোস্টের ওপরে তিন ডট (...) মেনুতে ক্লিক করে "Report Post" -> "Nudity or sexual activity" -> "Sharing private images" সিলেক্ট করুন।',
                'platformGuideEn': 'Click the three dots (...) on the post, select "Report Post" -> "Nudity or sexual activity" -> "Sharing private images".',
                'actionBtnBn': 'কোথায় জানাবেন দেখুন',
                'actionBtnEn': 'Where to Report',
                'displayOrder': 3,
            },
            {
                'slug': 'impersonation-and-fake-profiles',
                'titleBn': 'পরিচয় জালিয়াতি ও ভুয়া অ্যাকাউন্ট',
                'titleEn': 'Impersonation & fake profiles',
                'iconName': 'user-x',
                'immediateActionBn': 'আপনার নাম বা ছবি ব্যবহার করে ভুয়া প্রোফাইল খোলা হলে সেই প্রোফাইলের স্থায়ী লিংক (URL) ও স্ক্রিনশট সংরক্ষণ করুন এবং পরিচিতদের সতর্ক করে সরাসরি প্ল্যাটফর্মে Impersonation রিপোর্ট করুন।',
                'immediateActionEn': 'Copy the fake account\'s permanent profile URL and take screenshots of its posts before reporting it for impersonation on the platform.',
                'detailedStepsBn': 'ভুয়া প্রোফাইলটির মূল ইউআরএল (URL) কপি করুন এবং প্রোফাইল পেজ ও পোস্টগুলোর স্ক্রিনশট নিন।\nভুয়া আইডিটি আপনাকে ব্লক করে দেওয়ার আগেই অন্য একটি নিরাপদ বা বিশ্বস্ত অ্যাকাউন্ট থেকে প্রোফাইল লিংকটি সংরক্ষণ করুন।\nআপনার আসল প্রোফাইল থেকে একটি সংক্ষিপ্ত পোস্ট বা বার্তায় বন্ধু ও পরিবারকে সতর্ক করুন যেন কেউ ওই ভুয়া আইডির সাথে আর্থিক লেনদেন না করে।\nপ্ল্যাটফর্মে "Pretending to be me" অপশনে রিপোর্ট করুন এবং প্রয়োজনে সাইবার সাপোর্টে জানান।',
                'detailedStepsEn': 'Copy the permanent URL of the fake profile and screenshot its bio, photos, and posts.\nRecord the link using a trusted friend\'s account in case the fake profile blocks your main account.\nAlert your contacts privately or on your real profile not to engage or share money with the impersonator.\nSubmit an official "Pretending to be me" report on the platform and notify cyber support if harassment occurs.',
                'whatNotToDoBn': 'প্রমাণ (URL ও স্ক্রিনশট) সংরক্ষণ করার আগে ভুয়া আইডিটিকে মেসেজ দিয়ে সতর্ক করবেন না, তাহলে সে নিজের ইউজারনেম বদলে ফেলতে পারে।',
                'whatNotToDoEn': 'Do not message the fake account before capturing its URL and screenshots, as they may block you and change their handle.',
                'platformGuideBn': 'ভুয়া প্রোফাইলে গিয়ে তিন ডট (...) বাটনে ক্লিক করে "Find support or report profile" -> "Pretending to be someone" -> "Me" নির্বাচন করুন।',
                'platformGuideEn': 'Open the fake profile, click the three dots (...), select "Find support or report profile" -> "Pretending to be someone" -> "Me".',
                'actionBtnBn': 'প্ল্যাটফর্ম রিপোর্ট',
                'actionBtnEn': 'Platform Report',
                'displayOrder': 4,
            },
            {
                'slug': 'stalking-and-surveillance',
                'titleBn': 'স্টকিং ও নজরদারি',
                'titleEn': 'Stalking & surveillance',
                'iconName': 'eye',
                'immediateActionBn': 'অনলাইনে বা ডিভাইসে অনাকাঙ্ক্ষিত নজরদারি টের পেলে লোকেশন শেয়ারিং বন্ধ করুন, শক্তিশালী পাসওয়ার্ড ও টু-ফ্যাক্টর অথেনটিকেশন চালু করুন এবং প্রতিটি ঘটনার লগ সংরক্ষণ করুন।',
                'immediateActionEn': 'Review device permissions, disable live location sharing, enable two-factor authentication on another safe device, and document every stalking incident with timestamps.',
                'detailedStepsBn': 'আপনার ফোন ও সোশ্যাল মিডিয়া অ্যাপগুলোর লাইভ লোকেশন শেয়ারিং (Location Sharing) তাৎক্ষণিকভাবে বন্ধ করুন।\nগুগল, ফেসবুক ও ইমেইল অ্যাকাউন্টের "Active Sessions" বা "Where You\'re Logged In" চেক করে অপরিচিত সব ডিভাইস লগআউট করে দিন।\nএকটি নিরাপদ ডিভাইস থেকে সব পাসওয়ার্ড পরিবর্তন করুন এবং টু-ফ্যাক্টর অথেনটিকেশন (2FA) চালু করুন।\nস্টকারের প্রতিটি মেসেজ, কল বা গতিবিধির তারিখ ও সময় আমাদের ভল্টে ধারাবাহিকভাবে নোট করে রাখুন।',
                'detailedStepsEn': 'Turn off live location sharing across your phone settings, Google Maps, and social media apps immediately.\nCheck "Where You\'re Logged In" on your email and social accounts and log out of any unfamiliar devices.\nChange your passwords from a trusted device and enable Two-Factor Authentication (2FA).\nKeep a chronological log of every stalking attempt with dates, times, and screenshots in your vault.',
                'whatNotToDoBn': 'রিয়েল-টাইমে আপনি কোথায় আছেন (Check-in বা Live Story) তা সোশ্যাল মিডিয়ায় পোস্ট করবেন না।',
                'whatNotToDoEn': 'Do not post real-time location check-ins or stories while you are still at that physical location.',
                'platformGuideBn': 'ফোনের Settings -> Privacy -> Permission Manager-এ গিয়ে কোন কোন অ্যাপ আপনার Location, Camera এবং Microphone ব্যবহার করছে তা পরীক্ষা করে অপ্রয়োজনীয় পারমিশন বন্ধ করুন।',
                'platformGuideEn': 'Go to your phone Settings -> Privacy -> Permission Manager and revoke Location, Camera, and Microphone access from unknown apps.',
                'actionBtnBn': 'সহায়তা কেন্দ্র',
                'actionBtnEn': 'Get Support',
                'displayOrder': 5,
            },
            {
                'slug': 'doxxing-personal-info-exposed',
                'titleBn': 'ডক্সিং — ব্যক্তিগত তথ্য ফাঁস',
                'titleEn': 'Doxxing — personal info exposed',
                'iconName': 'file-warning',
                'immediateActionBn': 'ফোন নম্বর, বাসার ঠিকানা বা ব্যক্তিগত পরিচয়পত্র অনলাইনে ফাঁস হলে দ্রুত সেই পোস্টের স্ক্রিনশট ও লিংক সংরক্ষণ করুন। নিরাপত্তা ঝুঁকি থাকলে তাৎক্ষণিকভাবে ৯৯৯ বা পুলিশ সাইবার সাপোর্টে জানান।',
                'immediateActionEn': 'If your phone number, home address, or private documents are published online, preserve the URLs and screenshots immediately and contact emergency or cyber support.',
                'detailedStepsBn': 'যে পোস্টে বা পেজে আপনার ফোন নম্বর, ঠিকানা বা ব্যক্তিগত তথ্য ফাঁস করা হয়েছে, তার লিংক (URL) ও স্ক্রিনশট সংরক্ষণ করুন।\nঅপরিচিত নম্বর থেকে আসা কল বা মেসেজগুলোর স্ক্রিনশট রাখুন এবং ফোনে "Silence Unknown Callers" চালু করুন।\nব্যাংক বা মোবাইল ব্যাংকিং (বিকাশ/নগদ) তথ্য ফাঁস হয়ে থাকলে দ্রুত কাস্টমার কেয়ারে কল করে অ্যাকাউন্ট সুরক্ষিত করুন।\nবাসার ঠিকানা ফাঁস হলে এবং নিরাপত্তার ঝুঁকি মনে হলে তাৎক্ষণিকভাবে ৯৯৯ বা নিকটস্থ থানায় অবহিত করুন।',
                'detailedStepsEn': 'Save the exact URL and take full screenshots of the posts exposing your phone number, address, or private ID.\nDocument any harassing calls or texts from unknown numbers and enable "Silence Unknown Callers" on your phone.\nIf financial or mobile banking details were exposed, alert your provider immediately to secure your account.\nIf your physical address was shared and you feel unsafe, call 999 or inform local police right away.',
                'whatNotToDoBn': 'অপরিচিত নম্বর থেকে আসা কোনো ওটিপি (OTP) বা ভেরিফিকেশন লিংকে ক্লিক করবেন না।',
                'whatNotToDoEn': 'Never share OTP codes or click verification links sent by unknown callers claiming to help remove your info.',
                'platformGuideBn': 'ফেসবুকে ব্যক্তিগত তথ্য ফাঁস হলে পোস্টটি রিপোর্ট করার সময় "Sharing private information" অপশনটি বেছে নিন।',
                'platformGuideEn': 'When reporting a post that exposes your contact details or address, select "Sharing private information" in the report menu.',
                'actionBtnBn': 'জরুরি রিপোর্ট',
                'actionBtnEn': 'Emergency Report',
                'displayOrder': 6,
            },
        ]

        for item in situationsData:
            Situation.objects.update_or_create(slug=item['slug'], defaults=item)

        evidenceData = [
            {
                'stepNumber': 1,
                'stepLabelBn': '১',
                'instructionBn': 'স্ক্রিনশট নিন — তারিখ, সময় ও ইউজারনেমসহ।',
                'instructionEn': 'Screenshot everything with date, time, and username visible.',
            },
            {
                'stepNumber': 2,
                'stepLabelBn': '২',
                'instructionBn': 'মুছবেন না — আগে সংরক্ষণ করুন, তারপর ব্লক করুন।',
                'instructionEn': "Don't delete — first preserve, then block.",
            },
            {
                'stepNumber': 3,
                'stepLabelBn': '৩',
                'instructionBn': 'প্রোফাইল লিংক ও ইউআরএল কপি করে রাখুন।',
                'instructionEn': 'Save the profile link and URL.',
            },
            {
                'stepNumber': 4,
                'stepLabelBn': '৪',
                'instructionBn': 'বিশ্বস্ত কাউকে জানান — একা এই ভার বহন করবেন না।',
                'instructionEn': "Tell someone you trust — don't carry this alone.",
            },
        ]

        for step in evidenceData:
            EvidenceStep.objects.update_or_create(stepNumber=step['stepNumber'], defaults=step)

        fbProtocol = 'https://'
        fbPath = 'www.facebook.com/PCWSBD'

        channelsData = [
            {
                'channelType': 'emergency',
                'badgeBn': 'জরুরি',
                'badgeEn': 'Emergency',
                'titleBn': 'জাতীয় জরুরি সেবা',
                'titleEn': 'National Emergency Service',
                'phoneDisplayBn': '৯৯৯',
                'phoneDisplayEn': '999',
                'phoneDial': '999',
                'callBtnBn': '৯৯৯-এ কল করুন',
                'callBtnEn': 'Call 999',
                'iconName': 'phone-call',
                'displayOrder': 1,
            },
            {
                'channelType': 'helpline',
                'badgeBn': 'নারী ও শিশু',
                'badgeEn': 'Women & Children',
                'titleBn': 'জাতীয় হেল্পলাইন',
                'titleEn': 'National Helpline',
                'phoneDisplayBn': '১০৯',
                'phoneDisplayEn': '109',
                'phoneDial': '109',
                'callBtnBn': '১০৯-এ কল করুন',
                'callBtnEn': 'Call 109',
                'iconName': 'heart-pulse',
                'displayOrder': 2,
            },
            {
                'channelType': 'cyberPolice',
                'badgeBn': 'PCSW',
                'badgeEn': 'PCSW',
                'titleBn': 'PCSW – মহিলাদের জন্য পুলিশ সাইবার সহায়তা',
                'titleEn': 'Police Cyber Support for Women',
                'phoneDisplayBn': '01320000888',
                'phoneDisplayEn': '01320000888',
                'phoneDial': '01320000888',
                'email': 'cybersupport.women@police.gov.bd',
                'externalUrl': fbProtocol + fbPath,
                'iconName': 'shield-check',
                'displayOrder': 3,
            },
            {
                'channelType': 'platform',
                'titleBn': 'প্ল্যাটফর্ম রিপোর্ট',
                'titleEn': 'Platform report',
                'descriptionBn': 'ফেসবুক বা মেসেঞ্জারে সরাসরি "Report" বাটন ব্যবহার করুন।',
                'descriptionEn': 'Use the "Report" button directly on Facebook or Messenger.',
                'iconName': 'flag',
                'displayOrder': 4,
            },
            {
                'channelType': 'peerSupport',
                'titleBn': 'দ্য ফার্স্ট আওয়ার পিয়ার-সাপোর্ট',
                'titleEn': 'The First Hour peer support',
                'descriptionBn': '[ টিমের যোগাযোগ এখানে বসান ]',
                'descriptionEn': "[ Insert your team's contact here ]",
                'iconName': 'users',
                'displayOrder': 5,
            },
        ]

        for channel in channelsData:
            SupportChannel.objects.update_or_create(
                channelType=channel['channelType'],
                defaults=channel
            )

        self.stdout.write('Status: Toolkit data and detailed situation guides seeded successfully.')

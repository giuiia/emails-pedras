# E-mails Verão 26/27 · Pousada das Pedras · mesmo template dos e-mails da Black Friday 2026
import os, html
D = os.path.dirname(os.path.abspath(__file__))
OUT = D + '/emails'
IMG = 'https://raw.githubusercontent.com/giuiia/emails-pedras/main/Verao-2027/images/'
LOGO = 'https://raw.githubusercontent.com/giuiia/Pedras-EB/main/pedraslogo.png'
MOTOR = 'https://hbook.hsystem.com.br/Booking?companyId=62daa59f82345cb205532f55&amp;promocode=VERAO27&amp;utm_source=rdstation&amp;utm_medium=email&amp;utm_campaign=verao27&amp;utm_content='
WPP = 'https://wa.me/553534381133?text=Ol%C3%A1!%20Quero%20usar%20o%20cupom%20VERAO27%20da%20Pousada%20das%20Pedras%20e%20ver%20as%20datas%20livres.'
NOME = '*|FIRST_NAME|*'

def ent(s):
    # acentos em entidades, como nos e-mails da BF (mais seguro no RD)
    return ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in s)

P = '<p style="margin:0 0 18px;font-size:16px;line-height:1.65;text-align:center;">%s</p>'
def ps(*txt): return ''.join(P % t for t in txt)
def small(t): return '<p style="margin:0;font-size:14px;line-height:1.6;color:#6b7674;text-align:center;">%s</p>' % t

def bloco_texto(inner, pad='38px 44px 0px 44px'):
    return ('<tr><td class="px" align="center" style="padding:%s;font-family:\'Montserrat\',Arial,sans-serif;color:#3c4443;text-align:center;">%s</td></tr>' % (pad, inner))

def titulo(t):
    return '<p class="tt" style="margin:0 0 20px;font-family:\'Playfair Display\',Georgia,serif;font-size:28px;font-weight:bold;color:#0b0e0e;line-height:1.25;text-align:center;">%s</p>' % t

def cupom(extra=''):
    sub = '10% OFF' + (' &middot; ' + extra if extra else '')
    return ('<tr><td class="px" style="padding:10px 44px 0 44px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
            '<td align="center" bgcolor="#0b0e0e" style="border-radius:16px;padding:30px 24px;">'
            '<p style="margin:0 0 12px;font-family:\'Montserrat\',Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#ecc8a5;">Cupom de ver&#227;o</p>'
            '<table role="presentation" cellpadding="0" cellspacing="0" align="center"><tr><td align="center" style="border:2px dashed #ecc8a5;border-radius:10px;padding:12px 28px;">'
            '<p class="cod" style="margin:0;font-family:\'Montserrat\',Arial,sans-serif;font-size:38px;font-weight:700;color:#ffffff;line-height:1;letter-spacing:5px;">VERAO27</p></td></tr></table>'
            '<p style="margin:16px 0 4px;font-family:\'Montserrat\',Arial,sans-serif;font-size:20px;font-weight:700;color:#ecc8a5;line-height:1.3;">{SUB}</p>'
            '<p style="margin:0;font-family:\'Montserrat\',Arial,sans-serif;font-size:13px;color:#c9cfce;line-height:1.5;">Estadias de janeiro a mar&#231;o de 2027</p>'
            '</td></tr></table></td></tr>').replace('{SUB}', sub)

def botao(txt, utm, pad='26px 44px 6px 44px'):
    return ('<tr><td align="center" style="padding:%s;"><table role="presentation" cellpadding="0" cellspacing="0"><tr>'
            '<td align="center" bgcolor="#0b0e0e" style="border-radius:6px;">'
            '<a href="%s%s" target="_blank" style="display:inline-block;font-family:\'Montserrat\',Arial,sans-serif;font-size:15px;font-weight:bold;letter-spacing:.6px;text-transform:uppercase;color:#ecc8a5;text-decoration:none;padding:17px 38px;border-radius:6px;">%s</a>'
            '</td></tr></table></td></tr>') % (pad, MOTOR, utm, txt)

def botao_wpp():
    return ('<tr><td align="center" style="padding:8px 44px 4px 44px;"><table role="presentation" cellpadding="0" cellspacing="0"><tr>'
            '<td align="center" style="border:1.5px solid #0b0e0e;border-radius:6px;">'
            '<a href="%s" target="_blank" style="display:inline-block;font-family:\'Montserrat\',Arial,sans-serif;font-size:14px;font-weight:bold;letter-spacing:.6px;text-transform:uppercase;color:#0b0e0e;text-decoration:none;padding:14px 34px;border-radius:6px;">Chamar no WhatsApp</a>'
            '</td></tr></table></td></tr>') % WPP

def fotos3(itens):
    tds = ''.join('<td class="col3" width="33%%" style="padding:0 4px;"><img src="%s%s" width="165" alt="%s" style="display:block;width:100%%;height:auto;border-radius:10px;"></td>' % (IMG, f, a) for f, a in itens)
    return '<tr><td class="px" style="padding:26px 40px 0 40px;"><table role="presentation" width="100%%" cellpadding="0" cellspacing="0"><tr>%s</tr></table></td></tr>' % tds

def selos(itens):
    tds = ''.join('<td align="center" style="padding:0 6px;"><table role="presentation" cellpadding="0" cellspacing="0"><tr><td align="center" style="border:1.5px solid #0b0e0e;border-radius:10px;padding:12px 20px;font-family:\'Montserrat\',Arial,sans-serif;">'
                  '<p style="margin:0;font-size:26px;font-weight:700;color:#0b0e0e;line-height:1;">%s</p><p style="margin:6px 0 0;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#6b7674;">%s</p></td></tr></table></td>' % (n, l) for n, l in itens)
    return '<tr><td align="center" style="padding:4px 44px 22px 44px;"><table role="presentation" cellpadding="0" cellspacing="0"><tr>%s</tr></table></td></tr>' % tds

def selo_prazo(t):
    return ('<tr><td align="center" style="padding:30px 44px 0 44px;"><table role="presentation" cellpadding="0" cellspacing="0"><tr>'
            '<td align="center" bgcolor="#ecc8a5" style="border-radius:40px;padding:10px 24px;font-family:\'Montserrat\',Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:#0b0e0e;">%s</td></tr></table></td></tr>') % t

LEGAL = ('Cupom VERAO27: 10% OFF em reservas feitas de 01/12/2026 a 31/03/2027, para estadias de 01/01 a 31/03/2027. '
         'M&#237;nimo de 2 di&#225;rias, exceto feriados (Ano Novo e Carnaval, de 06 a 10/02/2027). Sujeito &#224; disponibilidade.')

def email(meta, banner, alt, corpo):
    head = '''<!--
============================================================
 VERAO 26/27 - %(codigo)s
 Disparo: %(quando)s
 Publico: %(publico)s
 ------------------------------------------------------------
 ASSUNTO:        %(assunto)s
 ASSUNTO (A/B):  %(ab)s
 PREVIEW TEXT:   %(preview)s
 ------------------------------------------------------------
 Assunto e preview NAO fazem parte do HTML: cole nos campos
 proprios do RD Station. O preview ja esta embutido como
 preheader oculto no inicio do corpo.

 IMAGENS: github.com/giuiia/emails-pedras > Verao-2027/images/
============================================================
-->
''' % meta
    return head + ('''<!DOCTYPE html>
<html lang="pt-BR" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>%s</title>
<!--[if mso]><style>* {font-family: Arial, sans-serif !important;}</style><![endif]-->
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Montserrat:wght@400;500;600;700&display=swap');
  body{margin:0;padding:0;background:#e9e6e1;}
  table{border-collapse:collapse;}
  img{border:0;display:block;line-height:100%%;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;}
  a{color:#0b0e0e;}
  @media only screen and (max-width:620px){
    .wrap{width:100%% !important;}
    .px{padding-left:22px !important;padding-right:22px !important;}
    .tt{font-size:25px !important;}
    .cod{font-size:30px !important;letter-spacing:3px !important;}
  }
</style>
</head>
<body>
<div style="display:none;max-height:0;overflow:hidden;opacity:0;mso-hide:all;font-size:1px;line-height:1px;color:#e9e6e1;">
  %s&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
</div>

<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" style="background:#e9e6e1;">
  <tr>
    <td align="center" style="padding:24px 12px;">
      <table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#ffffff;border-radius:14px;overflow:hidden;">

        <!-- FAIXA SUPERIOR -->
        <tr>
          <td align="center" style="background:#ecc8a5;padding:12px 24px;font-family:'Montserrat',Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:#0b0e0e;">
            Ver&#227;o nas montanhas &middot; 10%% OFF
          </td>
        </tr>

        <!-- CABECALHO: logo sobre preto -->
        <tr>
          <td align="center" style="background:#0b0e0e;padding:24px 24px;">
            <img src="%s" width="170" alt="Pousada das Pedras, Monte Verde, MG" style="width:170px;height:auto;margin:0 auto;">
          </td>
        </tr>

        <!-- BANNER -->
        <tr>
          <td style="padding:0;">
            <img src="%s%s" width="600" alt="%s" style="display:block;width:100%%;height:auto;">
          </td>
        </tr>

%s

        <!-- TEXTO LEGAL -->
        <tr>
          <td class="px" align="center" style="padding:24px 44px 34px 44px;font-family:'Montserrat',Arial,sans-serif;">
            <p style="margin:0;font-size:11px;line-height:1.6;color:#8a9492;text-align:center;">%s</p>
          </td>
        </tr>

        <!-- RODAPE -->
        <tr>
          <td align="center" style="background:#0b0e0e;padding:30px 24px;font-family:'Montserrat',Arial,sans-serif;">
            <img src="%s" width="140" alt="Pousada das Pedras" style="width:140px;height:auto;margin:0 auto 14px;">
            <p style="margin:0 0 10px;font-size:13px;color:#ecc8a5;"><a href="https://instagram.com/pousadadaspedrasmv" target="_blank" style="color:#ecc8a5;text-decoration:none;">@pousadadaspedrasmv</a></p>
            <p style="margin:0 0 10px;font-size:11.5px;color:#9aa5a3;line-height:1.6;">Rod. Dep. Agostinho Patrus, km 3, Distrito de Monte Verde, Camanducaia - MG</p>
            <p style="margin:0;font-size:11px;color:#9aa5a3;line-height:1.6;">&copy; 2026 Pousada das Pedras. Todos os direitos reservados.</p>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>
''') % (ent(meta['assunto']), ent(meta['preview']), LOGO, IMG, banner, ent(alt), corpo, LEGAL, LOGO)

H = '<span style="color:#b98a5c;">%s</span>'  # destaque areia escurecida (legível no branco)
E = []

# ---------- E1 ----------
def e1(abertura, codigo, arquivo, assunto, utm):
    corpo = (bloco_texto(titulo('Enquanto ' + H % 'a cidade ferve&#8230;') +
               ps(abertura,
                  'Nesse ver&#227;o, troque o calor e o tr&#226;nsito por um chal&#233; com hidromassagem, piscina com &#225;gua natural e caf&#233; da manh&#227; mineiro incluso, a 4 minutos do centro.')) +
             cupom() + botao('Reservar com 10% OFF', utm) +
             fotos3([('foto-piscina.jpg', 'Piscina da Pousada das Pedras'), ('foto-hidro.jpg', 'Hidromassagem do chal&#233;'), ('foto-cafe.jpg', 'Caf&#233; da manh&#227; mineiro')]) +
             bloco_texto(small('Estadias de janeiro a mar&#231;o de 2027. M&#237;nimo de 2 di&#225;rias, exceto feriados.'), '22px 44px 0 44px'))
    E.append((arquivo, email(dict(codigo=codigo, quando='03/12 (qui), 8h-10h, quentes primeiro', publico=('Cadastrados na LP da Black Friday que nao reservaram' if 'bf' in arquivo else 'Todos os segmentos, menos os cadastrados da BF (recebem a variacao)'),
              assunto=assunto, ab=('Suas férias de janeiro já têm destino?' if 'bf' not in arquivo else '(sem variação)'), preview='Cupom VERAO27 para estadias de janeiro a março de 2027.'),
              'banner-e1-lancamento.jpg', 'Piscina da Pousada das Pedras com vista para a serra', corpo)))

e1('Oi! Enquanto a cidade ferve, Monte Verde tem dias amenos, noites fresquinhas e lareira acesa.',
   'E1 - Lancamento: fuja do calor', 'e1-lancamento.html', 'Fuja do calor: 10% OFF no verão em Monte Verde', 'e1-lancamento')
e1('Oi! A Black Friday passou, mas o seu ver&#227;o na serra ainda pode sair com desconto. Por aqui, os dias s&#227;o amenos, as noites fresquinhas e a lareira fica acesa.',
   'E1 - Variacao cadastrados Black Friday', 'e1-lancamento-cadastrados-bf.html', 'Seu verão na serra ainda tem desconto', 'e1-lancamento')

# ---------- E2 ----------
corpo = (bloco_texto(titulo('Janeiro resolvido ' + H % 'antes das festas') +
           ps('Oi! Dezembro voa: confraterniza&#231;&#227;o, presentes, viagem de fam&#237;lia&#8230;',
              'E quando a gente v&#234;, janeiro chegou e as f&#233;rias ficaram sem plano.',
              'Que tal deixar isso resolvido agora? Uns dias na serra, com hidromassagem, lareira e caf&#233; da manh&#227; sem pressa.',
              'Pode ser at&#233; o <strong>presente de Natal de voc&#234;s dois</strong>.')) +
         cupom() + botao('Reservar com 10% OFF', 'e2-antes-das-festas') +
         bloco_texto(small('Estadias de janeiro a mar&#231;o de 2027. M&#237;nimo de 2 di&#225;rias, exceto feriados.'), '22px 44px 0 44px'))
E.append(('e2-antes-das-festas.html', email(dict(codigo='E2 - Resolva janeiro antes das festas', quando='15/12 (ter), 8h-10h', publico='Quentes, cadastrados BF, Leads LP, hospedes (NAO vai para a Base Geral)',
          assunto='Resolva as férias de janeiro antes das festas', ab='Um presente para vocês dois em janeiro', preview='10% OFF com o cupom VERAO27. Estadias de janeiro a março.'),
          'banner-e2-antes-das-festas.jpg', 'Chalé com lareira acesa na Pousada das Pedras', corpo)))

# ---------- E3 ----------
corpo = (bloco_texto(titulo('Quem j&#225; viveu, ' + H % 'recomenda') +
           ps('Escolher onde descansar &#233; mais f&#225;cil quando d&#225; para confiar.',
              'Na Pousada das Pedras, os h&#243;spedes mais elogiam o caf&#233; da manh&#227;, a vista das montanhas, a limpeza e o sil&#234;ncio.')) +
         selos([('4,7', 'Google'), ('9,3', 'Booking.com')]) +
         bloco_texto('<p style="margin:0 0 6px;font-family:\'Playfair Display\',Georgia,serif;font-style:italic;font-size:19px;line-height:1.5;color:#0b0e0e;text-align:center;">&#8220;O caf&#233; &#233; maravilhoso e o pessoal muito atencioso.&#8221;</p>'
                     '<p style="margin:0 0 22px;font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#8a9492;text-align:center;">Avalia&#231;&#227;o no Google</p>' +
                     ps('Nesse ver&#227;o, voc&#234; garante 10% OFF com o cupom VERAO27.'), '0 44px 0 44px') +
         cupom() + botao('Reservar com 10% OFF', 'e3-prova-social') +
         bloco_texto(small('Estadias de janeiro a mar&#231;o de 2027. M&#237;nimo de 2 di&#225;rias, exceto feriados.'), '22px 44px 0 44px'))
E.append(('e3-prova-social.html', email(dict(codigo='E3 - O que os hospedes mais elogiam', quando='05/01 (ter), 8h-10h', publico='Todos os segmentos',
          assunto='4,7 no Google, 9,3 no Booking e 10% OFF no verão', ab='O que quem já se hospedou mais elogia', preview='Café mineiro, vista da serra e silêncio. Cupom VERAO27.'),
          'banner-e3-prova-social.jpg', 'Café da manhã mineiro da Pousada das Pedras', corpo)))

# ---------- E4 ----------
corpo = (bloco_texto(titulo('Descanso n&#227;o &#233; s&#243; ' + H % 'no fim de semana') +
           ps('Oi! Sexta &#224; tarde na estrada, restaurante com fila, centrinho cheio&#8230;',
              'De <strong>domingo a quinta</strong>, Monte Verde &#233; outra viagem: estrada tranquila, piscina s&#243; para voc&#234;s e a serra em sil&#234;ncio.',
              'Todos os nossos chal&#233;s t&#234;m hidromassagem, lareira e caf&#233; da manh&#227; mineiro incluso. A <strong>Ala Prata</strong> &#233; a porta de entrada, com o melhor custo-benef&#237;cio da pousada.')) +
         cupom() + botao('Escolher minhas datas', 'e4-meio-de-semana') + botao_wpp() +
         bloco_texto(small('Estadias de janeiro a mar&#231;o de 2027. M&#237;nimo de 2 di&#225;rias, exceto feriados. O Carnaval (06 a 10/02) fica de fora.'), '22px 44px 0 44px'))
E.append(('e4-meio-de-semana.html', email(dict(codigo='E4 - Descanso de domingo a quinta', quando='19/01 (ter), 8h-10h', publico='Quentes, cadastrados BF, Leads LP, hospedes',
          assunto='Monte Verde de domingo a quinta é outra viagem', ab='Sem trânsito, sem fila: o verão no meio da semana', preview='10% OFF com o VERAO27 também no meio da semana.'),
          'banner-e4-meio-de-semana.jpg', 'Piscina e jardins da Pousada das Pedras', corpo)))

# ---------- E5 ----------
corpo = (bloco_texto(titulo('Depois do Carnaval, Monte Verde ' + H % 'fica assim&#8230;') +
           ps('Passadas as f&#233;rias e o Carnaval, a serra volta ao ritmo dela.',
              'Menos movimento, mais tranquilidade e a vista da Mantiqueira s&#243; para voc&#234;s. &#201; o melhor momento para quem quer descansar de verdade.',
              'Chal&#233; com hidromassagem e lareira, piscina e caf&#233; da manh&#227; mineiro incluso.')) +
         cupom('mar&#231;o') + botao('Reservar mar&#231;o com 10% OFF', 'e5-pos-carnaval') +
         bloco_texto(small('Estadias at&#233; 31 de mar&#231;o de 2027. M&#237;nimo de 2 di&#225;rias, exceto feriados.'), '22px 44px 0 44px'))
E.append(('e5-pos-carnaval.html', email(dict(codigo='E5 - Depois do Carnaval', quando='17/02 (qua), 8h-10h', publico='Todos os segmentos',
          assunto='Depois do Carnaval, Monte Verde fica assim…', ab='Março na serra: mais silêncio, mais vista, 10% OFF', preview='O cupom VERAO27 vale para estadias até 31/03.'),
          'banner-e5-pos-carnaval.jpg', 'Vista aérea da Pousada das Pedras e da Serra da Mantiqueira', corpo)))

# ---------- E6 + reenvio ----------
def e6(abertura, arquivo, codigo, quando, publico, assunto, ab, utm, banner, alt):
    corpo = (selo_prazo('Vale at&#233; 31/03') +
             bloco_texto(titulo('&#218;ltimos dias de ' + H % 'ver&#227;o na serra') +
               ps(abertura,
                  'Ele vale para reservas e estadias at&#233; <strong>31 de mar&#231;o</strong>. Ainda d&#225; tempo de uns dias de hidromassagem, lareira e caf&#233; mineiro antes de o ano engrenar de vez.',
                  'Se quiser, a gente confere as datas livres e te ajuda a escolher. &#201; s&#243; responder este e-mail ou chamar no WhatsApp.'), '24px 44px 0 44px') +
             cupom('at&#233; 31/03') + botao('Garantir meus 10% OFF', utm) + botao_wpp() +
             bloco_texto(small('M&#237;nimo de 2 di&#225;rias, exceto feriados.'), '22px 44px 0 44px'))
    E.append((arquivo, email(dict(codigo=codigo, quando=quando, publico=publico, assunto=assunto, ab=ab, preview='Depois de 31/03, a tarifa volta ao normal.'),
              banner, alt, corpo)))

e6('Oi! O ver&#227;o est&#225; acabando, e o cupom VERAO27 tamb&#233;m.', 'e6-ultima-chamada.html', 'E6 - Ultima chamada', '16/03 (ter), 8h-10h', 'Todos os segmentos',
   'Últimos dias: 10% OFF na serra até 31/03', 'O seu cupom de verão vence em 15 dias', 'e6-ultima-chamada', 'banner-e6-ultima-chamada.jpg', 'Vista aérea da Pousada das Pedras ao pôr do sol')
e6('Oi! Falta uma semana para o fim do cupom VERAO27.', 'e6-reenvio.html', 'E6 - Reenvio', '23/03 (ter), 8h-10h', 'So quem NAO abriu o E6',
   'Última semana do verão com 10% OFF', '(sem variação)', 'e6-reenvio', 'banner-e6-reenvio.jpg', 'Chalé de vidro da Pousada das Pedras com vista para a serra')

os.makedirs(OUT, exist_ok=True)
for nome, h in E:
    open(OUT + '/' + nome, 'w', encoding='utf-8').write(h)
print(len(E), 'e-mails')

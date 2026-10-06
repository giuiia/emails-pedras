# E-mails Black Friday 2026 · Pousada das Pedras

11 arquivos HTML prontos para colar na Edição Avançada do RD Station: os 8 e-mails do briefing, o FL1-pré, a variação "vence hoje" do FL3 e o reenvio do D3.

## Assunto e preview de cada e-mail

Esses campos não vão no HTML. Cole nos campos próprios do RD Station.

| Arquivo | Quando | Assunto | Assunto (teste A/B) | Preview |
|---|---|---|---|---|
| `fl1-cupom-imediato.html` | na hora do cadastro na LP (a partir de 01/11) | Seu cupom chegou: BLACK26 (até 40% OFF) | Pronto, seu cupom de 40% OFF está aqui | Estadias de janeiro a março de 2027. Reservas até 30/11. |
| `fl1-pre-cupom-reservado.html` | na hora do cadastro, so para cadastros ate 31/10 | Seu cupom da Black Friday está garantido | (sem variação) | Ele passa a valer em 01/11. Estadias de janeiro a março de 2027. |
| `fl2-a-experiencia.html` | 3 dias depois do FL1, so para quem nao reservou | Como é acordar na Pousada das Pedras | *|FIRST_NAME|*, seu cupom de 40% OFF continua com você | Hidromassagem, lareira e café mineiro, e a nota 4,7 no Google. |
| `fl3-lembrete-do-cupom.html` | 7 dias depois do FL1, nunca depois de 30/11. De 27 a 29/11 usar o assunto "Últimos dias do seu cupom BLACK26" | Seu cupom BLACK26 vale até 30/11 | Posso te ajudar a escolher a data, *|FIRST_NAME|*? | Até 40% OFF para estadias de janeiro a março de 2027. |
| `fl3-lembrete-vence-hoje.html` | 30/11 de manha, para cadastrados que nao reservaram | Hoje vence: seu cupom BLACK26 | (sem variação) | Até 40% OFF para estadias de janeiro a março de 2027. |
| `d1-abertura.html` | 01/11 (domingo, manha): Quentes primeiro, depois Leads LP 2025 e Base Geral | Black Friday na Pousada das Pedras: até 40% OFF no seu refúgio na serra | Aquela viagem a dois pode sair com até 40% OFF | Cadastre-se e receba o cupom na hora. Estadias de janeiro a março de 2027. |
| `d2-prova-social.html` | 12/11 (quinta): Base Geral + Leads LP que nao se cadastraram | 4,7 no Google, 9,3 no Booking, e agora com até 40% OFF | O que quem já se hospedou mais elogia | Café, vista, silêncio e hidromassagem. Cupom até 30/11. |
| `d3-black-friday-oficial.html` | 27/11 (sexta): Base Geral + Leads LP que nao se cadastraram (Fidelidade nao recebe) | Hoje é Black Friday: até 40% OFF no seu refúgio na serra | Black Friday chegou: o cupom vale até segunda (30/11) | Cadastre-se e receba o cupom na hora. |
| `d3-reenvio-cyber-monday.html` | 30/11 (segunda): so para quem nao abriu o D3 | Últimas horas: cadastre-se e garanta até 40% OFF | (sem variação) | Cadastre-se e receba o cupom na hora. |
| `f1-fidelidade-cupom-de-membro.html` | 17/11 (terca): base do Clube | Para quem é de casa: seu cupom de membro do Clube | Você faz parte do Clube, o CLUBE26 é seu | 40% OFF para estadias de janeiro a março de 2027. Válido até 28/11. |
| `f2-fidelidade-lembrete.html` | 25/11 (quarta): Fidelidade que nao reservou | Seu cupom CLUBE26 vence sábado (28/11) | Últimos dias do seu cupom de membro | 40% OFF para o seu próximo refúgio na serra. |

## Imagens no GitHub

Suba o conteúdo da pasta `images/` para `github.com/giuiia/emails-pedras`, dentro de `black-friday-2026/images/`.
Copie só os arquivos, sem arrastar a pasta inteira, para não criar pasta dentro de pasta.

Endereço base das imagens:
`https://raw.githubusercontent.com/giuiia/emails-pedras/main/black-friday-2026/images/`

## Links e rastreamento

- Divulgação (D1 a D3): botão "Quero meu cupom" leva para a LP.
- Fluxo 01 e Fidelidade: botão leva para o motor de reservas com o cupom aplicado (BLACK26 ou CLUBE26).
- Todos os links levam `utm_source=rdstation`, `utm_medium=email`, `utm_campaign=blackfriday2026` e o `utm_content` do briefing.

## Antes de disparar

- Testar cada botão e conferir se o cupom entra aplicado no motor de reservas.
- FL2 e os assuntos A/B de FL2 e FL3 usam a variável de primeiro nome do RD (`*|FIRST_NAME|*`). Conferir no teste de envio.
- Depoimento do D2: confirmar a autorização de uso.

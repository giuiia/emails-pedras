# E-mails Verão 26/27 · Pousada das Pedras

8 arquivos HTML no mesmo template da Black Friday, sem personalização de nome: os 6 e-mails do briefing, a variação do E1 para os cadastrados da Black Friday e o reenvio do E6.
Sem landing page: todos os botões abrem o motor de reservas com o **VERAO27** já aplicado.

## Assunto, preview e envio

Assunto e preview não vão no HTML. Cole nos campos próprios do RD Station (o preview já está embutido como preheader oculto).

| Arquivo | Quando | Público | Assunto | Assunto (teste A/B) | Preview |
|---|---|---|---|---|---|
| `e1-lancamento.html` | 03/12 (qui), quentes primeiro | Todos, menos os cadastrados da BF | Fuja do calor: 10% OFF no verão em Monte Verde | Suas férias de janeiro já têm destino? | Cupom VERAO27 para estadias de janeiro a março de 2027. |
| `e1-lancamento-cadastrados-bf.html` | 03/12 (qui) | Cadastrados na LP da Black Friday que não reservaram | Seu verão na serra ainda tem desconto | (sem variação) | Cupom VERAO27 para estadias de janeiro a março de 2027. |
| `e2-antes-das-festas.html` | 15/12 (ter) | Quentes, cadastrados BF, Leads LP, hóspedes (sem Base Geral) | Resolva as férias de janeiro antes das festas | Um presente para vocês dois em janeiro | 10% OFF com o cupom VERAO27. Estadias de janeiro a março. |
| `e3-prova-social.html` | 05/01 (ter) | Todos | 4,7 no Google, 9,3 no Booking e 10% OFF no verão | O que quem já se hospedou mais elogia | Café mineiro, vista da serra e silêncio. Cupom VERAO27. |
| `e4-meio-de-semana.html` | 19/01 (ter) | Quentes, cadastrados BF, Leads LP, hóspedes | Monte Verde de domingo a quinta é outra viagem | Sem trânsito, sem fila: o verão no meio da semana | 10% OFF com o VERAO27 também no meio da semana. |
| `e5-pos-carnaval.html` | 17/02 (qua) | Todos | Depois do Carnaval, Monte Verde fica assim… | Março na serra: mais silêncio, mais vista, 10% OFF | O cupom VERAO27 vale para estadias até 31/03. |
| `e6-ultima-chamada.html` | 16/03 (ter) | Todos | Últimos dias: 10% OFF na serra até 31/03 | O seu cupom de verão vence em 15 dias | Depois de 31/03, a tarifa volta ao normal. |
| `e6-reenvio.html` | 23/03 (ter) | Só quem não abriu o E6 | Última semana do verão com 10% OFF | (sem variação) | Depois de 31/03, a tarifa volta ao normal. |

Horário sugerido: 8h a 10h. Sem disparos de 22/12 a 03/01 e de 06 a 10/02 (Carnaval).

## Imagens no GitHub

Suba o conteúdo da pasta `images/` para `github.com/giuiia/emails-pedras`, dentro de `emails-verao-2027/images/`.
Copie só os arquivos, sem arrastar a pasta inteira, para não criar pasta dentro de pasta.

Endereço base das imagens:
`https://raw.githubusercontent.com/giuiia/emails-pedras/main/emails-verao-2027/images/`

Depois suba os HTMLs da pasta `emails/` e importe cada um no RD pelo link do arquivo.

## Links e rastreamento

- Botão principal: `https://hbook.hsystem.com.br/Booking?companyId=62daa59f82345cb205532f55&promocode=VERAO27&utm_source=rdstation&utm_medium=email&utm_campaign=verao27&utm_content=<código>`
- utm_content: `e1-lancamento` (também na variação BF), `e2-antes-das-festas`, `e3-prova-social`, `e4-meio-de-semana`, `e5-pos-carnaval`, `e6-ultima-chamada`, `e6-reenvio`.
- E4 e E6 têm também o botão "Chamar no WhatsApp" (35 3438-1133), com mensagem pronta citando o VERAO27.

## Antes de disparar

- Testar cada botão e conferir se o cupom continua aplicado no motor com as UTMs.
- Atualizar a supressão (BLACK26, BLACKADS26, CLUBE26 e VERAO27) antes de cada envio.
- Depoimento do E3 ("O café é maravilhoso e o pessoal muito atencioso."): confirmar que é de uma avaliação real no Google.
- Pendências do briefing com a Paulinha: cupom cumulativo ou não (texto legal) e datas do fluxo do Réveillon.

---
content_hash: 60072459e697d02263939c65a194056aa9c3b5012fdde972e5be5652ff5e7944
fetched_at: '2026-06-29T00:08:37.827281+00:00'
page_id: '284884294'
product: rm
source: tdn-rm
title: HTML -  Fixo
type: documentation
url: https://tdn.totvs.com/display/LRM/HTML+-++Fixo
version: 8
---

**Parametrizar Processo Seletivo para gerar Comprovante/Boleto de inscrição em HTML - Fixo**

A opção "HTML - Fixo" vai usar um modelo fixo de boleto em HTML e o comprovante será de acordo com o configurado no campo "Texto do comprovante de inscrição".

**1º-** Acesse os parâmetros do Processo seletivo na aba "Geral 2/3" e informe que o "Tipo do boleto/comprovante" seja "HTML - Fixo".

**TOTVS Processo Seletivo| Cadastros| Processo seletivo| Aba Parâmetros| Subseção Geral 2/3**

Assim o boleto exibido no portal do Processo Seletivo terá a estrutura conforme o modelo abaixo:

**2º-** Para gerar o comprovante, devemos configurá-lo na área "Texto do comprovante de inscrição" da aba "Geral 2/3".

Marcando a opção "Visualizar HTML", será possível ver o HTML gerado. Também pode ser copiado um texto em HTML pronto e salvar nesta área.

**3º-** Para configurar o Novo Portal para gerar o boleto fixo, é necessário configurar a URL do portal através do menu:

**Totvs Processo seletivo |****Ambiente | Parâmetros | Parâmetros Globais | Gerais | URL de acesso ao Portal RM.**

Importante

A partir da versão 12.1.2306 (junho/2023) não será necessário configurar a URL do Portal RM, o boleto gerado em HTML fixo já está disponível no portal padrão da FrameHTML e não utilizará mais nenhum recurso do antigo portal corpore.net.

Após a inscrição do candidato será exibido a tela para que ele gere o comprovante ou o boleto fixo.

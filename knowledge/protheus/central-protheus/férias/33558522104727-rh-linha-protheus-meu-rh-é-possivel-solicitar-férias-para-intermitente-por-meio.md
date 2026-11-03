---
article_id: 33558522104727
category: FÉRIAS
content_hash: 38418d58af390c8cf9ce772eb8b383cf6b58d900797e20a4d20b0d29134b4de4
fetched_at: '2026-06-28T22:44:34.478754+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - É possivel solicitar Férias para Intermitente
  por meio do MEU RH?
type: support-article
updated_at: '2026-06-18T18:06:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33558522104727-RH-Linha-Protheus-MEU-RH-%C3%89-possivel-solicitar-F%C3%A9rias-para-Intermitente-por-meio-do-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558516655895) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possivel solicitar férias para funcionários com tipo de contrato Intermitente por meio do MEU RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Não é possivel a solicitação de férias por meio do MEU RH para funcionários com contrato intermitente.  
  
A Contagem de dias de direito para funcionários com contrato Indeterminado/Determinado é feito através da rotina **Controle de Dias de** **Direito,** a qual é atualizada com o **fechamento** de cada período da folha de Pagamento.  
   
Contudo, como o funcionáriocom tipo de contrato **3 - Intermitente, recebe as férias proporcionais**a cada**convocação,** ou seja é pago diretamente na folha de pagamento o avo de direito de férias e 13º no fechamento de folha.  
  
[RH - Linha Protheus - GPE - Férias para funcionário intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493194-RH-Linha-Protheus-GPE-F%C3%A9rias-para-funcion%C3%A1rio-intermitente)  
  
Como não possui dados de DIAS a programar dentro do controle de dias de direito (**SRF**) o MEU RH não executará a programação.  
  
Mesmo que não haja saldo de férias convencional a ser processado, a rotina ainda gera uma estrutura dentro da tabela **SRF** como parte do processo padrão de cálculo efetuado dentro da folha de pagamento.  
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Há possibilidade de ser executado o cálculo de férias e 13º para funcionários com contrato intermitente através do roteiro 131 / 132 e rotina de cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038230414-RH-Linha-Protheus-GPE-H%C3%A1-possibilidade-de-ser-executado-o-c%C3%A1lculo-de-f%C3%A9rias-e-13%C2%BA-para-funcion%C3%A1rios-com-contrato-intermitente-atrav%C3%A9s-do-roteiro-131-132-e-rotina-de-c%C3%A1lculo-de-f%C3%A9rias)  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)

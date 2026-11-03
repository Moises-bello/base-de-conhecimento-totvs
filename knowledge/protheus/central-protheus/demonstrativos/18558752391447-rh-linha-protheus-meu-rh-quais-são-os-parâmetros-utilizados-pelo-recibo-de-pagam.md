---
article_id: 18558752391447
category: DEMONSTRATIVOS
content_hash: 60f4ecd290e60e4120733562d96c036bf155bcb2fa6b80fd8080dcfeb763716c
fetched_at: '2026-06-28T22:44:38.368231+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH - Quais são os parâmetros utilizados pelo Recibo
  de Pagamento do MEU RH
type: support-article
updated_at: '2026-06-22T19:14:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18558752391447-RH-Linha-Protheus-MEU-RH-Quais-s%C3%A3o-os-par%C3%A2metros-utilizados-pelo-Recibo-de-Pagamento-do-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18558789146519) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais são os parâmetros do Recibo de Pagamento através do MEU RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Segue lista dos parâmetros abaixo que, são referenciado de forma padrão:  
  
**MV\_IMPBASE** - Imprimir as Bases no Recibo de Pagamento gerado pelo aplicativo Meu RH. Onde .T. = imprime bases (padrão) e .F. = não imprime;  
**MV\_TCF013A** - Opções de consulta do demonstrativo de pagamento. 01-Adiantamento, 02-Folha, 03-1a parcela do 13o., 04-2a parcela do 13o. 05-Valores Extras, 06 - Autônomos e Pró-Labores e 07 - Valores Extras - roteiro VEX;  
**MV\_TCFCXFX** - Define quais campos serão exibidos sem diferença de maiúsculas e minúsculas nos dados cadastrais do RH Online;  
**MV\_TCFD131** - Define o dia do mês a partir do qual a 1ª. parcela do 13º. salário está liberada para consulta no Meu RH;  
**MV\_TCFD132** - Define o dia do mês a partir do qual a 2ª. parcela do 13º. salário está liberada para consulta do 13º. salário está liberada para consulta no Meu RH;  
**MV\_TCFDADT** - Define o dia do mês a partir do qual o adiantamento está liberado para consulta no App Meu RH;  
**MV\_TCFDEMO** - Indica se utiliza o *rdmake* RECIBO.PRX na visualização do recibo de pagamento no App Meu RH, sendo 1=Utiliza o *rdmake*; 2=Utiliza o fonte padrão;  
**MV\_TCFDEXT** - Define o dia do mês a partir do qual os valores extras e PLR estão liberados para consulta no App Meu RH;  
**MV\_TCFDFOL** - Define a quantidade de dias que será somada, ou subtraída, à data de pagamento do roteiro FOL, para formar o dia a partir do qual está liberada consulta no App Meu RH;  
  
Abaixo, **demais parâmetros que podem ser utilizados**, se o *RDMAKE* RECIBO.prx for **customizado**:  
**MV\_AGLUTPD** - Agrupa verbas na impressão do recibo de pagamento, sendo: 1-Aglutina verbas / 2-Nao Aglutina;  
**MV\_EMCONTA** - Indica qual conta utilizada para envio de e-mails automáticos pelo sistema;   
**MV\_EMSENHA** - Indica qual a senha da conta utilizada para envio de e-mails automáticos pelo sistema;   
**MV\_GPEMAIL** - *E-mail* do Responsável pelo Departamento Pessoal destinado a receber alertas, quando ocorrer erro em processamentos de rotinas, processos e relatórios;  
**MV\_RELSERV** - Nome do Servidor de Envio de E-mail utilizado nos relatórios;  
**MV\_RELT** - Diretório especificado para impressão de relatórios;  
**MV\_IREFSEM** - Define se na referência das verbas de aulas serão: "S"- Impresso número aulas semanais; "N"- impresso total de aulas no mês.  
  
**Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**

---
article_id: 360029134994
category: GPE - eSocial - Periódicos
content_hash: 370e946b27f27e2dc101fa1b7848ca64a3f6fc61bc1b78e32d49970e3c46c621
fetched_at: '2026-06-28T22:45:07.523282+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial -  S-1200 - Como preencher informações
  relativas a períodos anteriores diretamente no TAF
type: support-article
updated_at: '2025-07-21T15:01:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029134994-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-preencher-informa%C3%A7%C3%B5es-relativas-a-per%C3%ADodos-anteriores-diretamente-no-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26962853848599) Tempo aproximado para leitura: 00:02:30 min****Ocorrência**Como preencher informações relativas a períodos anteriores diretamente no TAF  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**A necessidade de preencher as informações manualmente no TAF é de vontade e responsabilidade exclusiva da Empresa e seu usuário do Sistema. Um dos cenários mapeados que origina essa necessidade é a **opção do usuário em não utilizar a rotina do SIGAGPE para cálculo do Dissidio/Reajuste Retroativo**.  
  
**Solução**Alimentar a informação manualmente no TAF:  
  
**Observação:** O conteúdo e consistência dessas informações é de responsabilidade exclusiva da Empresa e seu usuário do Sistema, a TOTVS não se responsabiliza pelas informações manipuladas/preenchidas em cada campo, sendo o intuito dessa documentação explicar a dependência das informações dentro da rotina.  
  
**Passo 1:** Acesse SIGATAF: *Atualizações > Eventos eSocial > Periódicos > Folha de Pagamento (TAFA250):*  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041960534)  
  
**Passo 2:** Selecione a opção Incluir ou Alterar algum registro já existente.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042802233)  
  
**Passo 3:** Vá até a aba **Demonstrativo de Valores** e certifique-se de já existir alguma **Identificação do Demonstrativo de Valores** conforme esperado pelo [leiaute do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica), até esse passo você pode se basear nas informações de outros eventos S-1200 que tenha em sua base de dados, mas o TAF não realiza validações e a consistência das informações deverá ser analisada de acordo com o esperado pelo leiaute do eSocial.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041962554)  
  
**Passo 4:** A partir deste momento você selecionará a aba **Informações Relativas a Remuneração do Trabalhador em Períodos Anteriores ao Período de Apuração**, o preenchimento deverá ser pela ordem das informações na rotina do TAF e de acordo com o leiaute do eSocial.  
  
**Informações do Acordo:** Originalmente o Sistema busca essas informações das tabelas S050 e S126 do SIGAGPE, bem como das informações preenchidas na rotina do **SIGAGPE para cálculo do Dissidio/Reajuste Retroativo**.  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042803973)**O campo **Descrição** é obrigatório pelo leiaute e ao dar duplo click sobre o termo MEMO o Sistema vai abrir uma caixa onde poderá preencher a descrição, a mesma informação da tabela S126 do SIGAGPE. **![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042804433)  
  
Informações do Período:**Originalmente é preenchida com as informações do cálculo da rotina do SIGAGPE para cálculo do Dissidio/Reajuste Retroativo (tabela RHH).   
  
Basicamente é a relação dos períodos a qual o Dissidio/Reajuste retroage e abaixo de cada período será detalhado o seu pagamento.  
 **![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042804633)**  
**Informações do Estabelecimento/Lotação:**Originalmente é preenchida com as informações do cálculo da rotina do SIGAGPE para cálculo do Dissidio/Reajuste Retroativo (tabela RHH).   
  
Nesses campos são informados os dados do estabelecimento e lotação tributária do período a qual o Dissidio/Reajuste retroage.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042805333)  
  
**Informações da Remuneração do Trabalhador no Período de Apuração:**Originalmente é preenchida com as informações do cadastro do Trabalhador do SIGAGPE (tabela SRA), com exceção do campo Competência Acordo e Contribuição Substituída, vide help (F1).   
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042805553)  
  
**Itens da Remuneração do Trabalhador:** Originalmente é preenchida com as informações do cálculo da rotina do SIGAGPE para cálculo do Dissidio/Reajuste Retroativo (tabela RHH).   
  
Basicamente é um detalhamento da diferença que o Trabalhador tem direito no período informado em "**Informações do Período"**. Para sabe mais sobre o que o SIGAGPE traz para esse campo acesse o artigo: [RH - Linha Protheus - GPE - eSocial - S-1200 - Quais verbas serão enviadas para o eSocial nos casos de Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852).  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042806793)  
  
**Passo 5:** Preenchidas as informações acima o evento estará disponível no monitoramento do TAF para envio ao eSocial.  
  
**ATENÇÃO:** A ausência de informações em qualquer um dos itens acima pode ocasionar em erros nas rotinas do TAF ou erros de *schema* no envio ao eSocial.  
  
**Saiba Mais**Para adquirir mais conhecimento acesse os *links* abaixo:   
[Como gerar informações de dissidio e rescisão complementar por dissidio no esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271)   
[Quais os prazos para envio de S-1200, S-1210 e S-1299 referentes à folha anual e Como informar período de apuração anual no evento S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020493932)   
[Como o eSocial vai apurar os encargos nos casos de Reajuste/Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342453)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*

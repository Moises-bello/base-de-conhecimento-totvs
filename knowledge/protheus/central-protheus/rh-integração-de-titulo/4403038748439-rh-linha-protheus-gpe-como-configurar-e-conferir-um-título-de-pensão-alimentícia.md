---
article_id: 4403038748439
category: RH - Integração de Titulo
content_hash: 7801f6eedf33f1b124caea5e529310f678fe15aad92e7b1cdb0189c6b13f68d3
fetched_at: '2026-06-28T22:43:36.194045+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar e conferir um título de Pensão
  Alimentícia
type: support-article
updated_at: '2025-07-15T20:34:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403038748439-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-de-Pens%C3%A3o-Aliment%C3%ADcia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33489922964375)**Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como configurar e conferir um título de Pensão Alimentícia?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1) Acesse **Miscelânea** -> **Títulos** -> **Definição**:  
![10.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33489931734167)

2) Preencher os campos da definição de título:  
**Atenção:** os campos preenchidos no exemplo abaixo são meramente ilustrativos.   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403032411543)

Selecionando a opção Pensão Alimentícia, o sistema efetua a busca automática das verbas e roteiros na execução da rotina  **Geração de Títulos - GPEM670**, sendo assim você já pode pular para o tópico 6 desta documentação, caso selecione a opção **Definido pelo Usuário**, continue a leitura do Documento.  
  
3) No canto inferior direito, clicar em "**Definir Título**" para selecionar as verbas e a tabela onde será coletada a informação:   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403038486807)  
  
4)  Na definição de título, especificar a verba para geração e a tabela para busca dos valores. No exemplo abaixo, apresentamos as verbas de pensão alimentícia e a busca na tabela **SRC - Movimento do período**, uma vez que o movimento de adiantamento ainda não foi fechado, se a parametrização for para um título de Pensão Alimentícia sobre **Férias** ou **Rescisão** deverá ser selecionada a tabela **SRR - Itens de Férias e Rescisão**.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403032657687)  
Nos pagamentos de Pensão Alimentícia quando existe mais de um beneficiário para o mesmo funcionário é necessário criar novas verbas para que seja possível cadastrar o novo beneficiário, sendo assim todas as verbas criadas para desconto no Roteiro deverão ser selecionadas.

**Atenção:**A legenda da  verba selecionada para geração deverá ser verde para que seja considerada na geração. Legendas vermelhas são consideradas como dedução do valor.

**Obs:** Importante atentar-se no momento da geração do título, na configuração da verba nesta definição. Se o movimento de folha esta aberto, a busca de verbas de folha deverá ocorrer na tabela **SRC (Movimento do período)** e caso o movimento de folha esteja fechado a busca será na tabela **SRD (Histórico de movimento)**.

5) Após a criação do título, verificar no resumo de folha de pagamento , os valores calculados referentes à verba indicada na definição de título:   
Acesse: **Relatórios** -> **Periódicos** -> **Folha de Pagamento**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403032879127)

 6) Acessar **Miscelânea** -> **Títulos** -> **Geração**, configurando os campos de acordo com a definição de título e datas de geração.  
  
7) Verificar na manutenção de títulos, o título gerado com o valor de acordo com o resumo de folha:  
Acessar: **Miscelânea** -> **Títulos** -> **Manutenção**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403038675351)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como configurar o título de pensão automaticamente com dados do beneficiário como fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025329234-RH-Linha-Protheus-GPE-Como-configurar-o-t%C3%ADtulo-de-pens%C3%A3o-automaticamente-com-dados-do-benefici%C3%A1rio-como-fornecedor-)

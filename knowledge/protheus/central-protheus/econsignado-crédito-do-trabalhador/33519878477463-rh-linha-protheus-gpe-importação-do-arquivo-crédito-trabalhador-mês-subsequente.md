---
article_id: 33519878477463
category: eConsignado (Crédito do Trabalhador)
content_hash: d6d99f1a50ee6a08eea5178d7be0f0491541e4f49432d7a1853d8a4e56ccbd74
fetched_at: '2026-06-28T22:43:07.121501+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês
  subsequente ao período de calculo aberto - mais de um contrato - eConsignado MP(1.292/2025)
type: support-article
updated_at: '2026-05-20T13:15:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33519878477463-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-subsequente-ao-per%C3%ADodo-de-calculo-aberto-mais-de-um-contrato-eConsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33519850418839) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar a importação do arquivo do mês subsequente ao período de calculo aberto ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Foi um implantada a rotina GPEM944A Credito Trabalhador, para adequar o sistema para importação do arquivo gerado pelo governo no Portal Emprega Brasil referente ao eConsignado quando o colaborador possui mais de um contrato de empréstimo.  
A rotina suporta somente **arquivos .CSV** e **.JSON**. e para a importação é necessário:

**1**. Criar novas verbas para o desconto dos demais contratos. Ex. 4 contratos, 4 verbas.   
o sistema passou a comportar até 50 verbas, sendo a verba principal e mais 49 novas verbas.   
Abaixo exemplo de importação com mais de um contrato.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33519850420119)  
  
2. Informar as verbas na tabela S154.   
Para ter a nova tabela é necessário aplicar o ultimo pacote do RH expedição continua   
12.1.2310 COM GARANTIA ESTENDIDA APENAS: <https://suporte.totvs.com/portal/p/10098/download?e=1123885>  
12.1.2310 com fontes até 30.06 para clientes **SEM** garantia estendida: <https://suporte.totvs.com/portal/p/10098/download?e=1204698>  
12.1.2410 = <https://suporte.totvs.com/portal/p/10098/download?e=1170810>  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33519878448791)  
  
3. Ter o novo Grupo de perguntas GPM944A. (criado com a aplicação da atualização)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33519878450071)  
  
4. Nesse exemplo vamos importar a competência 08/2025 ainda com a competência 07/2025 aberta para calculo.   
- Cadastro do período 07/2025  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33519850422551)  
  
- Cadastro do período 08/2025 - no qual vai ser feita a importação.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33519878460951)  
  
5. Importação  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33519878461591)  
  
6. Após gravar o sistema vai apresentar a mensagem de validação no campo Observação  
- O empréstimo foi gravado somente no histórico RUO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40608444316567)  
  
7. A visualização da RUO é possível através da consulta genérica, para isso é necessário indicar a tabela dentro da consulta, para isso siga as orientações do artigo [RH - Linha Protheus - GPE - Como configurar a tabela RUO para que seja demonstrada em consulta genérica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32722175502871-RH-Linha-Protheus-GPE-Como-configurar-a-tabela-RUO-para-que-seja-demonstrada-em-consulta-gen%C3%A9rica)  
Em consultas> cadastro> genéricos, é possível validar a importação.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33519850424215)

**Importante**  
Para realizar a importação do mês seguinte **não deve ser feito ajuste do campo período selecionado no cadastro dos períodos** (atual e mês seguinte). Se o período atual for deixado = não e o seguinte = sim, o Sistema vai **sobrepor** os dados já gravados para o mês atua de forma indevida, causando inconsistência nos cálculos.

**Para maior conhecimento assista os videos How To abaixo:**

**Saiba Mais:**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)  
[Econsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=944703898>

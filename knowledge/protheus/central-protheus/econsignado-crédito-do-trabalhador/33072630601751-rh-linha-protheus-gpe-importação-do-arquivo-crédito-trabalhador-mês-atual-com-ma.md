---
article_id: 33072630601751
category: eConsignado (Crédito do Trabalhador)
content_hash: 6fea8c920c8e2d6ce1cb88214f1e5559711c3d05068db70d1e33e9f1647c1cf6
fetched_at: '2026-06-28T22:43:07.113055+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês
  atual  com mais de um contrato- eConsignado MP(1.292/2025)
type: support-article
updated_at: '2026-05-19T17:53:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33072630601751-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-atual-com-mais-de-um-contrato-eConsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33072640620823) Tempo aproximado para leitura: **00:03:00min**  
  
**Dúvida**  
Como realizar a importação do arquivo Crédito trabalhador mês atual  quando existe mais de um contrato- Econsignado MP(1.292/2025)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Foi um implantada a rotina GPEM944A Credito Trabalhador, para adequar o sistema para importação do arquivo gerado pelo governo no Portal Emprega Brasil referente ao Econsignado quando o colaborador possui mais de um contrato de empréstimo.  
A rotina suporta somente **arquivos .CSV** e **.JSON**. e para a importação é necessário:

**1**. Criar novas verbas para o desconto dos demais contratos. Ex. 4 contratos, 4 verbas.   
o sistema passou a comportar até 50 verbas, sendo a verba principal e mais 49 novas verbas.   
Abaixo exemplo de importação com mais de 1 contrato.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35135118775447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33072630581271)

2. Atrelar as verbas na tabela S154.   
Para ter a nova tabela é necessário aplicar o ultimo pacote do RH expedição continua   
12.1.2310 COM GARANTIA ESTENDIDA APENAS: <https://suporte.totvs.com/portal/p/10098/download?e=1123885>  
12.1.2310 com fontes até 30.06 para clientes **SEM** garantia estendida: <https://suporte.totvs.com/portal/p/10098/download?e=1204698>  
12.1.2410 = <https://suporte.totvs.com/portal/p/10098/download?e=1170810>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40589225477271)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40589225480343)

3. Ter o novo Grupo de perguntas GPM944A. (criado com a aplicação da atualização)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33072630582039)

4. Realizar a importação do arquivo  (como exemplo utilizamos o tipo de arquivo Json)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33512461621911)

Após clicar em gravar , os valores são levados para Lançamentos futuros (SRK) e Histórico de Importação (RUO)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40589252961303)

5.  Lançamentos Futuros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40589225485975)

**Regra para compor o valor de desconto quando há mais de um contrato**  
Valores importados serão ordenados de acordo com a data de inicio do empréstimo (RUO\_DTINIC), enquanto valores lançados manualmente serão ordenados pela data de movimentação e número de documento (RK\_DTMOVI e RK\_DOCUMEN).  
  
Da mesma forma que foi limitado o valor do segundo contrato, pode acontecer do primeiro contrato ultrapassar o limite e calcular proporcional, nessa situação não será calculado o segundo contrato pois o limite já atingiu no primeiro, e em casos que nenhum dos contratos atingir o limite de desconto, será calculado integral.

**Para maior conhecimento assista os vídeos How To abaixo:**

**Saiba Mais:**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)  
[Econsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=944703898>

---
article_id: 360022683891
category: RH - Relatórios
content_hash: 9ef532598179b390e832a4493c42c045bc5b275eca58e99041bfc02551ad92e0
fetched_at: '2026-06-28T22:44:43.536681+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Espelho de ponto imprime Folha em branco
type: support-article
updated_at: '2026-04-01T11:44:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022683891-RH-Linha-Protheus-PON-Espelho-de-ponto-imprime-Folha-em-branco
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35617305360663) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
O que verificar quando o Espelho de Ponto imprime folha em branco?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões.  
  
**Solução**  
Para solucionar quando o sistema não lista as informações no espelho de ponto segue as orientações abaixo:  
  
**Obs**. Para contas das tabelas **SP8** e/ou **SPG** as consultas poderão serem feitas através da rotina de consulta genérica, por se tratarem de tabelas da base de dados.  
Para consultar a documentação sobre a consulta genérica [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060836073-RH-Linha-Protheus-GPE-Como-gerar-tabela-em-planilha-em-Consulta-Gen%C3%A9rica)

- Faça a validação dos passos abaixo, em caso de período **Fechado**:  
1 - Deve existir **marcações** do funcionário na **SPG;**  
2 - Na **SPG**, confira se o conteúdo do campo **PG\_PAPONTA** está de acordo com o **período**, exemplo: se o período era de 01 à 30.11.2021, o conteúdo do campo deve estar desta forma: **2021110120211130**  
3 - Verificar se existe **Troca de Turno** para o funcionário no **primeiro dia do período** em questão, se não, insira manualmente  
4 - No cadastro de período, é necessário existir um **registro com o período fechado**  
5 - Acesse a rotina de **Acumulados de Marcações** e verifique se consegue ver as marcações do período em questão. Veja com acessar nesta documentação: [RH - Linha Protheus - PON - Como visualizar as marcações de períodos já fechados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060589393-RH-Linha-Protheus-PON-Como-visualizar-as-marca%C3%A7%C3%B5es-de-per%C3%ADodos-j%C3%A1-fechados)  
6 - Se conseguir visualizar as **marcações** no **Acumulado de Marcações**, gere o **Espelho de Ponto do período desejado.**

- Faça a validação dos passos abaixo, em caso de período **Aberto**:  
1- Deve existir **marcações** do funcionário na **SP8;**  
2 - Na **SP8**, confira se o conteúdo do campo **P8\_PAPONTA** está de acordo com o **período**, exemplo: se o período é de 01 à 30.11.2021, o conteúdo do campo deve estar desta forma: **2021110120211130**  
3 - Verificar se existe **Troca de Turno** para o funcionário no **primeiro dia do período** em questão, se não, insira manualmente  
4 - Verificar se o conteúdo do parâmetro **MV\_PAPONTA** está com o dia **inicial/final** do período, exemplo: se o período é de 01 à 30.11.2021, o conteúdo do **parâmetro** deve estar **01/31** (isso permite que o cliente consiga trabalhar com mais de um período futuro em aberto, apenas alterando a data base do Protheus)  
5 - Verificar se a **data base do Protheus** está no **último dia do período**, exemplo: se o período é de 01 à 30.11.2021, a data base deve estar em 30.11.2021  
6 - Fazer o **Cálculo Mensal** do período  
7 - Gerar o **Espelho de Ponto**  
  
  
  
**Saiba Mais:**  
[RH - Linha Protheus - PON - Como trabalhar com dois Períodos de Apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026360652-RH-Linha-Protheus-PON-Como-trabalhar-com-dois-Per%C3%ADodos-de-Apontamento?source=search)  
[RH - Linha Protheus - PON - Espelho de Ponto em Duplicidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021518871-RH-Linha-Protheus-PON-Espelho-de-Ponto-em-Duplicidade?source=search)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)

---
article_id: 38860017145111
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0e6f47dbaa3cbd74def052cc820eac61e10bbdac2d0f909422d2d74be03c747f
fetched_at: '2026-06-28T22:37:22.897439+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CN300SLDFIS ao
  realizar uma Revisão de Contrato
type: support-article
updated_at: '2026-03-06T18:51:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38860017145111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CN300SLDFIS-ao-realizar-uma-Revis%C3%A3o-de-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38860017140375) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao realizar uma Revisão de Contrato ocorre o help CN300SLDFIS.

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Referente a ocorrência do help CN300SLDFIS, conforme o funcionamento padrão da rotina CNTA300, o sistema  realiza uma varredura dos itens da planilha e faz a verificação em cada item da planilha do contrato, onde para o item verificado no momento, ele faz a subtração abaixo, e se:  
   
**CNS\_RLZQTD (Qtd Medida no Cronograma Físico) - CNB\_QTDMED (Qtd Medida no Item da planilha do contrato) > 0,01**  
   
Nessa situação ocorre o help CN300SLDFIS.

Sobre a ocorrência do help, é importante se validar no ambiente em questão se os campos do processo do Gestão de Contratos estão com seus tamanhos e casas decimais de acordo e consistentes uns com os outros nas tabelas do SIGAGCT, conforme as orientações do artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os campos a serem considerados no ajuste de casas decimais das tabelas do Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022576132-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-campos-a-serem-considerados-no-ajuste-de-casas-decimais-das-tabelas-do-Gest%C3%A3o-de-Contratos)

Estando com os campos de acordo e condizentes entre si, no caso do contrato em específico, um teste que pode ser realizado é a execução em ambiente de homologação do recálculo dos saldos do contrato.Conforme as instruções do artigo abaixo, verificando se é modificado alguma informação/comportamento ou se ainda persiste:  
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Ajuste de Saldos em Contratos, Planilhas e Cronograma Financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Ajuste-de-Saldos-em-Contratos-Planilhas-e-Cronograma-Financeiro-?source=search)

Caso a situação ainda persista para o contrato em específico, outro teste que pode ser realizado em ambiente de homologação é: Caso a empresa não utilize a gestão e controle de cronograma físico de contrato em seu processo, recomenda-se realizar o cadastro/ajuste do contrato com o Tipo de Contrato/Planilha configurado com o campo ‘Cronog. Fis.= Não’.(E juntamente a manutenção da tabela CNS sem possuir dados nessa tabela de Cron. Físico pra esse contrato conforme configurações do tipo de contrato/planilha ajustados).Conforme é recomendado uso do sistema neste caso em que a empresa não possui este controle em seu processo. Visto que essa configuração de cronograma físico no contrato, é orientada ser utilizada apenas caso a empresa possua este tipo de controle em seu processo.  
E neste teste verificando se a questão ainda assim persiste.  
   
**Obs:**  
Toda e qualquer manutenção em base de dados, orienta-se a realização por um analista especialista em loco com conhecimento e realização sempre primeiramente em homologação para validação do processo.

***Saiba Mais:***

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

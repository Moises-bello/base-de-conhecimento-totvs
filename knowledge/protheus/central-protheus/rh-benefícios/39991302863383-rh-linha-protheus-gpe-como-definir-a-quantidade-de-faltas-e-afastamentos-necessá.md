---
article_id: 39991302863383
category: RH - Benefícios
content_hash: c704906bd04fa60d404ed7e005878b8b6f39dcb1d6b97657133b246304faef1b
fetched_at: '2026-06-28T22:44:03.750808+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como definir a quantidade de faltas e afastamentos
  necessários para efetuar o desconto de benefícios VT/VR/VA
type: support-article
updated_at: '2026-04-24T17:12:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39991302863383-RH-Linha-Protheus-GPE-Como-definir-a-quantidade-de-faltas-e-afastamentos-necess%C3%A1rios-para-efetuar-o-desconto-de-benef%C3%ADcios-VT-VR-VA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39991302835223) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como definir a quantidade de faltas e afastamentos necessários para efetuar o desconto de benefícios VT/VR/VA?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Foi criado o mnemônico **P\_NVAFABEN**, cujo conteúdo padrão é **.F**., e que servirá para definir se o novo controle de faltas será utilizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39991331176343)

Criada também a tabela de gestão de faltas e afastamentos **S153** na rotina **Manutenção de Tabelas**, onde será possível definir quais eventos de faltas e tipos de ausências serão descontados, bem como a quantidade mínima do evento para que o desconto ocorra.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39991302839831)

**Filial:** Define para qual filial a regra será valida. Deixe em branco para que seja aplicada para todas as filiais.  
**Cód. CCT:** Define para qual convenção coletiva a regra será valida. Deixe em branco para que seja aplicada para todas as CCT's.  
**Ev. Ponto:** Informe os eventos de falta do ponto eletrônico que farão parte da regra.   
**Tp. Ausência:** Informe os tipos de afastamento que farão parte da regra. Se informado asterisco ("\*") serão considerados todos os afastamentos.  
**Qtd. Máx.** Ocorrências: Informe a quantidade máxima de faltas e atrasos (a soma de todos os eventos) poderá ocorrer antes de ser efetuado desconto.  
**Cód. Abono:** Informe os códigos de abono que anulam eventuais faltas, se não for informado nenhum, qualquer falta informa no campo "Ev. Ponto" será considerada, mesmo que abonada.  
**Qtd. Máx. Abono:** Informe a quantidade máxima de abonos que deve ser considerada antes de efetuar o desconto.  
**Roteiro:** Informe para quais roteiros a regra será valida.  
**Desc Total ou Saldo?:** Informe se o desconto será feito pelo total de faltas e afastamentos apurados ou pelo saldo, quando o total for maior que a quantidade máxima de ocorrências permitida.  
**Código do Benefício:** Informar o código do benefício que será validado no cálculo.

**Importante:** Ao ativar o mnemônico **P\_NVAFABEN**, os demais tratamentos pré-existentes para faltas e afastamentos serão ignorados, como por exemplo a utilização do mnemônico **P\_BENPONEV** para faltas**,** devendo toda regra ser definida na tabela **S153**, caso não existam regras definidas e o mnemônico esteja ativo, nenhuma falta/afastamento será descontado.

Apenas **eventos do ponto** serão **considerados para busca de faltas**. O mnemônico **P\_BENBUSFA** continuará sendo usado para buscar as faltas no período atual ou anterior do ponto, independente da configuração do parâmetro **MV\_USACPER**, pois só será buscado as **faltas do SIGAPON**.

Além do mnemônico e da configuração da tabela **S153**, é necessário que os parâmetros **"Desconta Faltas"** e **"Desconta Afastamentos"** dos roteiros de cálculo VT/VR/VA estejam com valor diferente de **"Não"**. Especificamente com relação ao parâmetro **"Desconta Afastamentos"**, não fará diferença ele esta configurado para "Afastamentos/Férias/Ambos" uma vez que a definição do tipo de afastamento será efetuada dentro da tabela S153.

**Saiba Mais**  
[Gestão de Faltas e Afastamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=896206447#body-body1)  
[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)

---
content_hash: fa85097b818d4812fabe12bf6e18870a9a53702021b6951cccd90f029b9369ef
fetched_at: '2026-06-29T00:11:37.442381+00:00'
page_id: '777928132'
product: rm
source: tdn-rm
title: DT - Bloquear a visualização do Total da Remuneração da Base AAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777928132
version: 7
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Ficha Financeira |
| Função: | Ficha Financeira - Base AAS |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHCALCRM-4603](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-4603) |

## **02. VERSÕES**

**Versões:**

* + **12.1.2310.1**

## **03. SITUAÇÃO/REQUISITO**

Criar no cadastro de permissões de acesso a campos a opção de habilitar / desabilitar a visualização das informações do Total da Remuneração da BASE AAS, pois hoje não temos a opção de ocultar as informações salariais do funcionário.

## **04. SOLUÇÃO**

Foi adicionado a funcionalidade que bloqueia a visualização do Total da Remuneração, essa funcionalidade foi adicionada na **BASECONTRIBUICAO** na tabela **PFAAS** no acesso a campos em perfil de segurança.  
  
Quando o botão **Pode Consultar** estiver inativo não será permitido a visualização do Total da remuneração na Base AAS, já quando o botão **Pode Alterar** estiver inativo não será permitido que seja Gerado ou Excluído o Grupo 0 - AAS.

**05. EXEMPLO**

Parâmetros Marcados, Parâmetro Pode Consultar Desmarcado, Parâmetro Pode Alterar Desmarcadopasso1,passo2,passo3yespasso1

BASECONTRIBUICAO com todas as flags ativas:

nopasso2

BASECONTRIBUICAO com a flag Pode Consultar inativa:

nopasso3

BASECONTRIBUICAO com a flag Pode Alterar inativa:

    

## **06. ASSUNTOS RELACIONADOS**

* [Ficha Financeira](https://tdn.totvs.com/display/public/LRM/Ficha+Financeira)
* [Segurança - Perfis](https://tdn.totvs.com/pages/releaseview.action?pageId=146182940)

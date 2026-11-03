---
content_hash: 2eb5255f58e04453703b0464741960b253d70302a865ac7fe359610743be6b44
fetched_at: '2026-06-29T00:11:27.660857+00:00'
page_id: '728640552'
product: rm
source: tdn-rm
title: DT - Processos - Buscar Retenção Lei 9.711/98 do EFD-REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=728640552
version: 5
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Processos - Buscar Retenção Lei 9.711/98 do EFD-REINF |
| País: | Brasil |
| Release: | 12.1.2302 |
| Issue: | DRHROTRM-5100 |

## **02. SITUAÇÃO/REQUISITO**

Ter o valor de retenção conforme Lei 9.711/98 do sistema Gestão Fiscal, para realizar a geração do "Relatório de Conferência INSS Patronal" e lançamento financeiro da DCTFWeb.

## **03. SOLUÇÃO**

Disponibilizado o parâmetro "**Buscar Retenção Lei 9711/98 do EFD-Reinf**" em Configurações | Parametrizador | eSocial | Gerais 4/7.

Ao marcá-lo o sistema irá buscar o valor de retenção conforme lei 9.711/98 do sistema Gestão Fiscal.

O sistema buscará essa informação através de um serviço que retorna o valor gerado pelo REINF no Evento R-5011 (Retorno do Evento R-2099 - Fechamento). 

## **04. DEMAIS INFORMAÇÕES**

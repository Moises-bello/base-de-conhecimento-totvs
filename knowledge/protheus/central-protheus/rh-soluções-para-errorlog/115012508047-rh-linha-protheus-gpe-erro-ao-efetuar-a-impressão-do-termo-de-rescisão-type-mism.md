---
article_id: 115012508047
category: RH - Soluções para error.log
content_hash: 799066d605ddedbfd935bbd76112f7f572936f28813b807aa8b8a0d53fea386a
fetched_at: '2026-06-28T22:44:08.837530+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro ao Efetuar a Impressão do Termo de Rescisão:
  type mismatch on compare  on FCABEC(IMPRESH.PRW)'
type: support-article
updated_at: '2025-08-21T18:39:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115012508047-RH-Linha-Protheus-GPE-Erro-ao-Efetuar-a-Impress%C3%A3o-do-Termo-de-Rescis%C3%A3o-type-mismatch-on-compare-on-FCABEC-IMPRESH-PRW
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34352277493911)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Ao realizar o **cálculo de Rescisão**, através da rotina **GPEM040**, é apresentado ***error log***: ***type mismatch on compare on* FCABEC(IMPRESH.PRW)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Utilização de *RDMake* IMPRESH.PRW desatualizado.  
 **Solução**  
**1.** Baixar o pacote de RDMakes mais atualizados no Portal, conforme abaixo:  
[MP - GPE - Como fazer o download (baixar) os RDMAKES de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044814174-MP-GPE-Como-fazer-o-download-baixar-os-RDMAKES-de-RH?source=search)  
**2.** Compilar o RDMake IMPRESH.PRW contido no pacote, no ambiente.  
 **Importante**  
Caso esteja com o RPO muito desatualizado, além de aplicar o pacote de RDMAKE acima, será necessário atualizar também o pacote acumulado da sua versão conforme a Base de Conhecimento:  
[MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)  
 **Saiba Mais:**  
Pacote Acumulado e-Social:  
[MP - GPE - Como fazer o download (baixar) do pacote de acumulado do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial?source=search)

---
article_id: 39584601782807
category: Integrações Outros BackOffice
content_hash: 4ab7dbbc6a5667092bf238da21e42f307076a59aefa04eb8ee20acd43aa3a908
fetched_at: '2026-06-28T22:46:42.084287+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RH - RM - FOP - Integração RM Labore x BackOffice Protheus: A empresa e filial
  constantes na Business Content'
type: support-article
updated_at: '2026-04-10T14:09:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39584601782807-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-A-empresa-e-filial-constantes-na-Business-Content
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39584601773335) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao tentar realizar a integração, o serviço EAI retorna a seguinte mensagem de erro: “A empresa e a filial informadas no Business Content não possuem correspondência cadastrada no Protheus.”  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O erro ocorre quando a Coligada e a Filial enviadas pelo RM no XML não possuem um relacionamento (DE/PARA) devidamente configurado com o Grupo de Empresa e a Filial correspondentes no Protheus.  
  
**Solução**  
O DE/PARA de empresa/filial enviado no XML está incorreto ou inexistente.

Primeiramente, obtenha o XML Transformado e Identifique qual a Coligada e Filial que estão sendo enviados para o Protheus através da documentação: [**RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Obtenção o XML mensagem de Resposta e Transformada no RM**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036176914-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Obten%C3%A7%C3%A3o-o-XML-mensagem-de-Resposta-e-Transformada-no-RM)

No sistema RM, é necessário acessar **Integração | EAI 2.0 | DE/PARA** e verificar se há o cadastro correto para a tabela **GCOLIGADA**, responsável por definir qual coligada será integrada a determinado Grupo de Empresa.

Nessa mesma tela, também deve ser conferida a tabela **GFILIAL**, que estabelece a correspondência entre **Coligada/Filial do RM e Grupo de Empresa/Filial no Protheus.**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/39584539642263)**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39584539642519)

Caso não exista um DE/PARA devidamente configurado para coligada e filial do RM em relação ao Grupo de Empresa e Filial do Protheus em ambos os sistemas, a mensagem de erro será retornada.

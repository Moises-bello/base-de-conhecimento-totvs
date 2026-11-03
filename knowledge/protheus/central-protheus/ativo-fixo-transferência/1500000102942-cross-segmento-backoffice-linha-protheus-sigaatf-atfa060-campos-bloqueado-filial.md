---
article_id: 1500000102942
category: Ativo Fixo - Transferência
content_hash: 160c32cfb7f7ceacf30254fb4569fb35d77a751e0f84cf55e0fde64a1cd17775
fetched_at: '2026-06-28T22:41:52.158616+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 - CAMPOS BLOQUEADO
  (FILIAL,CONTA..)
type: support-article
updated_at: '2023-12-01T15:03:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000102942-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-CAMPOS-BLOQUEADO-FILIAL-CONTA
---

**Dúvida**

Ao realizar a transferência do bem o campo Filial e ou conta estão bloqueados

Ao tentar fazer a transferência de alguns bens o sistema não habilita os campos das contas contábeis de destino.  
  
**Ambiente**Microsiga Protheus – Ativo Fixo – A partir da versão P11

**Solução**

Uma das possibilidades para esta ocorrência é devido ao campo N1\_PROJETO estar preenchido e o campo N1\_REVPROJ estar em branco.

Na rotina de transferências ATFA060 existe uma validação que verifica o conteúdo destes campos. Caso estejam na situação acima descrito, o sistema somente irá habilitar o campo Destino para ser alterado, os demais estarão desabilitados.

O campo N1\_PROJETO não é novo, mas antigamente não existia nenhuma validação para ele. Por este motivo, alguns clientes conseguiam colocar um número de projeto para seu controle interno.

Atualmente foi desenvolvido a rotina [**Projeto Imobilizado (ATFA430)**](https://tdn.totvs.com/display/public/PROT/ATFA0034_Cadastro+de+Projeto+do+Imobilizado) para atender uma parte da interpretação técnica ICPC 01 Contratos de Concessão e que utiliza o campo N1\_PROJETO para seu controle. Essa nova rotina está focada no controle de projetos de despesas sem margem de receita e não possui integração com o módulo de Gestão de Projetos (SIGAPMS).

Por conceito da rotina Projeto do Imobilizado (ATFA430) não e possível fazer alterações contábeis na rotina de transferência.

O cliente que estiver utilizando o campo N1\_PROJETO, mas que não tem nenhuma relação com a nova rotina, deverá decidir se permanece ou se retira a informação do campo N1\_PROJETO para conseguir fazer a alteração das informações contábeis desejadas.

Saiba mais:

[MP - SIGATF -ATFA060 TRANSFERÊNCIA CIAP COMO FAZER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033898193-MP-SIGATF-ATFA060-TRANSFER%C3%8ANCIA-CIAP-COMO-FAZER?source=search)

[MP - SIGAATF - POSSIBILIDADES VÁLIDAS PARA PREENCHIMENTO DO CAMPO MESES Cl. PIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021278592-MP-SIGAATF-POSSIBILIDADES-V%C3%81LIDAS-PARA-PREENCHIMENTO-DO-CAMPO-MESES-Cl-PIS?source=search)

[MP - SIGATF - CAMPOS DO ATIVO BLOQUEADOS - N1\_CODCIAP - N1\_ICMSAPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011054291-MP-SIGATF-CAMPOS-DO-ATIVO-BLOQUEADOS-N1-CODCIAP-N1-ICMSAPR-?source=search)

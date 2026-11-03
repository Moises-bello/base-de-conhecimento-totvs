---
content_hash: 11f16af8d4dcd5a84ca7265df103781600751e0e72e814f1428575b6fa33e788
fetched_at: '2026-06-29T00:10:09.991897+00:00'
page_id: '452719772'
product: rm
source: tdn-rm
title: Concluir Etapa
type: documentation
url: https://tdn.totvs.com/display/LRM/Concluir+Etapa
version: 3
---

**Concluir Etapa**

Ao executar este processo a etapa é finalizada, alterando o seu status para "Concluído", e altera o status da próxima etapa, se existir, de "Não Iniciada" para "Em Andamento".

**Observação:**

Ao concluir a etapa o sistema oferece a possibilidade de enviar email (relatório ou texto livre) para os candidatos aprovados e reprovados na etapa concluída.

Ao iniciar a execução deste processo o sistema fará a seguintes validações:

1 - Se o parâmetro "Requisição obrigatória para admissão" estiver marcado e existir alguma solicitação (que não seja requisição) vinculada ao Perfil de Vaga o usuário será avisado que o processo de admissão ou movimentação ocorrerá apenas com o uso de requisições.

2 - Se não existir nenhuma requisição/solicitação, com vagas a serem preenchidas, vinculadas ao perfil de vaga o usuário será avisado que o processo de pesquisa não será interrompido, mas não será possível admitir o candidato.

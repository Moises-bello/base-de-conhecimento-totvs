---
content_hash: 413d17fe4d8b68d2ee4612afcb04d8b616927587a2ec7d0b74db9b10ab5d73fb
fetched_at: '2026-06-29T00:09:33.348606+00:00'
page_id: '425458990'
product: rm
source: tdn-rm
title: Classificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458990
version: 5
---

---

Nesta opção cadastra-se a tabela de classificação do atendimento.

Através do cadastro é possível controlar:

**Identificação**

Nesta pasta, serão informados os dados que identificarão a classificação cadastrada.

Código de classificação:

Código identificador da classificação. Este código é único e é criado automaticamente pelo sistema.

Descrição da classificação:

Neste campo deve ser informado o nome (descrição) da classificação. Ex.: Defeito, Dúvida, Instalação, etc.

Permite alterar classificação:

Essa opção permite a definição da alteração de uma determinada classificação.

Essa permissão pode ser realizada tanto no cadastro da classificação quanto em:

Cadastros | Segurança | Perfis | Acesso a Campos | Tabela "HATENDIMENTOEXT" | Campo CODCLASSIFICACAO.

Para que o campo classificação da ocorrência seja alterado é necessário verificar a regra abaixo:

Quem abriu a ocorrência -> Pode alterar;

Atendente é chefe (direta ou indiretamente) de quem está com a ocorrência   
  
 Se tiver permissão (via perfil do usuário) -> Pode alterar   
  
 Se não tiver permissão (via perfil do usuário) -> Altera dependendo do tipo de classificação

Atendente não é chefe   
  
 Atendente é o responsável (atendente está com a ocorrência) pelo atendimento   
  
 Tipo da classificação permite -> Pode alterar   
  
 Tem permissão (via perfil do usuário) -> Pode Alterar   
  
 Atendente não é o responsável (atendente está com a ocorrência) -> Não pode alterar   
  
 Nível de acesso  
Preencha neste campo, o nível de acesso que a ocorrência terá caso a mesma possuir esta classificação. O atendente só enxergará os atendimentos com nível de acesso menor ou igual ao seu, ou atendimentos com nível de acesso superior, desde que este atendimento esteja sob a responsabilidade do atendente.

**Atenção!**

O campo Nível de cesso na classificação é um valor default (padrão) onde a ocorrência receberá este valor assim que for criada. 

O nível de acesso de uma ocorrência pode ser alterado manualmente apenas pelos chefes definidos em Cadastros | Hierarquia. 

Ao se trocar à classificação de uma ocorrência, o sistema verificará se o nível de acesso que está definido na mesma foi inserido ao ser criado a ocorrência ou se foi alterado pelo usuário manualmente. Caso foi inserido na criação da ocorrência, o sistema fará a troca do nível da ocorrência pelo nível da nova classificação que está sendo inserida. Caso o usuário tenha alterado o nível na edição da ocorrência manualmente, o sistema não altera o nível que está na ocorrência mantendo o mesmo independente de qual nível pertence à classificação que está sendo alterada. 

**Classificação ativa:**

Selecione esta opção caso deseja que a classificação que está sendo cadastrada seja exibida na lista de opções do campo Classificação do atendimento. Por algum motivo, com o decorrer do tempo, uma classificação pode ser desativada, ou seja, inutilizada. Neste caso, pode-se desmarcar esta opção tornando a classificação inativa. Neste momento, os atendimentos que estiverem com esta classificação continuarão, mas os novos não vão possuí-la.

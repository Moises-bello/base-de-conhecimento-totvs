---
content_hash: e801655b7d21ecdd32b8cb1bee9f94c83d5c960ed9832829f0de2bcb16f33a39
fetched_at: '2026-06-29T00:08:35.556061+00:00'
page_id: '281981967'
product: rm
source: tdn-rm
title: 723032 EDUCACIONAL01-132 Atualização de dados do Certificado e Registro no
  Livro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281981967
version: 104
---

# CERTIFICADO/DIPLOMA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Atualização de dados do Certificado e Registro no Livro |
| **Situação/Requisito:** | O usuário não consegue alterar o campo “Data de registro” no menu Certificados/Diploma do Registro em Livro. Também solicita permitir que a alteração seja realizada em LOTE e também ser controlada por permisões no Perfil do usuário. |
| **Solução/Implementação:** | Otimização no Certificado/Diploma, onde foi criado o processo “Atualização de dados do Certificado e Registro no Livro” para permitir alterações globais no certificado e no registro no livro do certificado.  - Nome da action deste processo: EduAlteracaoGlobalRegistroNoLivroAction.  - Necessário recriar o broker.dat.  - Somente será habilitado este processo, se marcado no Perfil do usuário a permissão de acesso ao mesmo (Atividades Acadêmicas | Certificado/Diploma | Certificados/diplomas | Atualização de dados do Certificado e Registro no Livro).  - Será permitido alterar somente alguns campos que são editáveis e que não tenham tratamentos específicos. Dados do Certificado: data do certificado e carga horária; Dados do Registro no Livro: data de conclusão, data conferência, data de emissão, data de registro.  - O campo “Data de Registro” atualmente não é editável no sistema, para permitir sua alteração é necessário marcar a opção “Permitir alterar data de registro do Registro no Livro do Certificado” no anexo “Parâmetros educacionais” do perfil do usuário. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs

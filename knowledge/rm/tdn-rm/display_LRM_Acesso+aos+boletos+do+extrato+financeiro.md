---
content_hash: c981125716982fca177c727a1c79471ea2e64bdd74298f2bb3d9f19b80842fc5
fetched_at: '2026-06-29T00:11:33.274062+00:00'
page_id: '754954981'
product: rm
source: tdn-rm
title: Acesso aos boletos do extrato financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/Acesso+aos+boletos+do+extrato+financeiro
version: 36
---

**A partir da versão 12.1.2402.247, 12.1.2406.188 e 12.1.2410.124** foram feitas alterações de comportamento relacionadas a visualização do extrato financeiro no portal para nos adequar a LGDP.

* O usuário visualizará somente os boletos onde ele é responsável financeiro direto.  
  O sistema faz a validação, se o usuário logado no portal é o responsável financeiro da parcela do contrato do aluno.
* Somente o aluno conseguirá visualizar **todos os boletos do contrato**

Será exibido um parâmetro no anexo do contrato do aluno, que deve ser habilitado pela instituição caso o responsável financeiro do boleto deseja dar permissão de acesso aos dados para o pai e/ou mãe, responsável acadêmico e responsável financeiro pelo aluno. 

* No Acesso dados Contrato estiver o marcado o "Permitir Acesso": o usuário pode visualizar todos boletos do aluno, independentemente de quem seja o responsável financeiro.
* No Acesso dados Contrato estiver o desmarcado o "Permitir Acesso" o usuário pode visualizar somente os boletos onde ele é responsável financeiro direto.

Configuramos o acesso aos dados financeiros do aluno na visão dos responsáveis do cadastro do aluno, conforme mostrado abaixo.

Caso o extrato financeiro seja acessado por um usuário diferente do aluno, é imprescindível para a identificação correta dos boletos que o campo "Usuário de acesso" esteja vinculado no cadastro de Cliente/Fornecedor.

ATENÇÃO

É **imprescindível** que o **Responsável Financeiro** já possua o **"Usuário de Acesso"** vinculado em seu cadastro de cliente/fornecedor **antes** de ser associado ao aluno.

Caso o Responsável Financeiro informado no cadastro do aluno não tenha esse vínculo de acesso, a permissão deve ser concedida posteriormente: marque o campo **"Permitir Acesso"** na aba **"Acesso dados Contrato"** e salve no contrato do aluno.

Foi disponibilizado um parâmetro para habilitar a permissão para pais (Pai e Mãe), Responsável Acadêmico terem acesso aos dados Financeiros dos alunos independente da permissão concedida. Trata-se de um parâmetro por perfil de usuário, e o mesmo está disponível no módulo Educacional

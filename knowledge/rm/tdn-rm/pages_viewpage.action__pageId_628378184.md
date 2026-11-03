---
content_hash: 6979120794cc207e0cce190a59d73317f4da40aae4a5ef2c9c0450b2ef47a792
fetched_at: '2026-06-29T00:11:05.263980+00:00'
page_id: '628378184'
product: rm
source: tdn-rm
title: Pendências de matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628378184
version: 25
---

Na central do candidato, será exibido um alerta caso o aluno que realizou a matrícula via central do candidato possua alguma pendência de documentação ou pagamento dessa matrícula.

Importante

Esta funcionalidade estará disponível somente na versão 12.1.33.

A partir das versões **12.1.33.216, 12.1.34.126 ou superiores**, as pendências de matrículas não serão exibidas para **matrículas canceladas**. Ou seja, caso o aluno matriculado esteja com uma situação de matrícula no período letivo com o campo "**Aluno ativo**" DESMARCADO, as pendências de matrículas (Documentos e/ou Pagamentos) não serão disponibilizadas na central do candidato.

Localização do campo de indicação de matrícula cancelada: *TOTVS Educacional | Currículo e Oferta | Aluno | Anexo Matrícula no período letivo | Situação de matrícula | Aba Status no período letivo | Aluno ativo.*

1 - Documentos

Caso o documento seja rejeitado através dos , ao acessar a central de candidatos será possível fazer o reenvio desse documento.

2 - PagamentosImportante

Esta funcionalidade estará disponível somente na versão **12.1.33.103** ou superior.

Será considerada uma pendência de pagamento se o lançamento financeiro da primeira parcela do contrato do aluno estiver em aberto.

Regras

* Pendência de pagamento não se aplica a processo seletivo do tipo “Venda Online”
* A primeira parcela será a de menor vencimento e que possuir boleto gerado.
* Caso o contrato possua mais de uma parcela/boleto com o mesmo vencimento e pelo menos um boleto esteja baixado, então não será considerado que o aluno possui uma pendência de pagamento.
* Assim que o aluno realizar o pagamento da 1º parcela e for realizado a baixa do lançamento, a opção de pendência por pagamento não será mais exibida na central do candidato.

Na central do candidato, quando existir uma pendência de pagamento será apresentada a mensagem conforme mostrada na figura abaixo:

Ao clicar no botão "Pagamentos" na central do candidato, será apresentada uma tela com as informações das parcelas disponíveis para o pagamento.

As formas de pagamento (Cartão, Pix ou Boleto) exibidas serão habilitadas conforme as parametrizações definidas no cadastro do serviço vinculada a parcela selecionada.

Informação

Caso a 1º parcela esteja vencida, a pendência de pagamento estará disponível mas não será possível realizar o pagamento através da central do candidato, sendo o candidato/aluno orientado a entrar em contato com a instituição:

Importante

A partir da versão **12.1.2205** o processo passa a ter a seguinte mudança:

Quando a primeira parcela estiver vencida poderá ocorrer as seguintes situações:

* Candidato/aluno/responsável que possuir um usuário de acesso ao Portal do Aluno já vinculado no seu cadastro de pessoa no RM. Será exibido uma mensagem informando que ele pode atualizar e pagar seu boleto através do Portal do Aluno tendo também um "Clique aqui" para redirecionar o aluno. Para que essa mensagem e o redirecionamento sejam executados com sucesso, é necessário configurar a URL do FrameHTML disponibilizada no RM → Ambiente → Parâmetros → Parâmetros globais → Aba FrameHTML.

* Aluno ainda não possui um usuário de acesso ao Portal do Aluno vinculado ao seu cadastro de pessoa no RM ou a URL do FrameHTML não foi configurada nos parâmetros globais. Será exibido uma mensagem informando que o aluno deve procurar a instituição.

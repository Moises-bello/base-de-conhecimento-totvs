---
content_hash: ec257dc412b9749d41445899616effbb8380d0e34ce71d54bb21f748d2a14b1a
fetched_at: '2026-06-29T00:09:33.959551+00:00'
page_id: '425459094'
product: rm
source: tdn-rm
title: Verificar a inadimplência na transferência interna e por coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459094
version: 9
---

A validação da inadimplência do aluno será feita conforme o parâmetro presente no processo de transferência interna:

Para a Transferência Interna**,**o parâmetro "Transferir aluno inadimplentes" ficará disponível para seleção conforme a marcação dos parâmetros **Bloquear matrícula para inadimplentes** (Configurações | Parâmetro | Matricula | Movimento 1/4) e  **Permitir transferência de alunos inadimplentes** (Perfil | Educacional | Anexos | Parâmetros Educacionais), funcionando da seguinte forma:

* Parâmetro do TOTVS Educacional “**Bloquear matrícula para inadimplentes**” estiver desmarcado a transferência é realizada com sucesso mesmo o aluno estando inadimplente. Neste cenário, o parâmetro "**Transferir alunos inadimplentes****"** é apresentado desabilitado e marcado nos processos de transferência interna.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula para inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Permitir transferência de alunos inadimplentes**” marcada, neste cenário é exibido nos processos de transferência interna o parâmetro "**Transferir alunos inadimplentes****"** sendo possível marcar e desmarcá-lo**:**
  + Se estiver desmarcado, a inadimplência é verificada e se o aluno estiver inadimplente a transferência não é realizada.
  + Se estiver marcado, a transferência é realizada mesmo o aluno estando inadimplente.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula para inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Permitir transferência de alunos inadimplentes**” desmarcada, a inadimplência é verificada e se o aluno estiver inadimplente a transferência não é realizada. Neste cenário o parâmetro "**Transferir alunos inadimplentes****"**é apresentado desabilitado e desmarcado nos processos de transferência interna.

Nesse sentido, com as duas parametrizações marcadas, a instituição de ensino pode escolher validar ou não a inadimplência do aluno durante o processo de transferência interna, seja essa transferência dentro da mesma filial, entre filiais ou entre coligadas.

Atenção

Alguns parâmetros que constam no sistema influenciam a execução desta funcionalidade, assim é necessário avaliar sua configuração, são eles:

* Matrícula - Bloquear mudança de situação de matrícula para inadimplentes - responsável por definir se o sistema executará a validação de inadimplência quando o cenário for de alteração da situação de matrícula.
* Tesouraria - Verificar débitos do aluno em outras coligadas - determina se a validação de inadimplência será apenas no âmbito da coligada corrente ou levará em consideração todas as coligadas do sistema.
* Tesouraria - Número de dias de carência para inadimplência -  determina a partir de quantos dias de atraso no pagamento o sistema passa a considerar como inadimplência.
* Tesouraria - Valor máximo de tolerância para inadimplência - determina um valor teto para que o aluno ainda não seja considerado inadimplente.
* Tesouraria - Valor máximo da conta corrente de tolerância para inadimplência - de forma similar ao item anterior no entanto com relação aos valores da conta corrente do aluno.
* Validar inadimplência na bolsa - Se a opção '*Verifica inadimplência do outro sacado*' estiver marcada na bolsa que possui outro sacado (Bolsa de crédito), será feita a validação da inadimplência do "Outro sacado", e impedirá a transgênica, caso "Transferir alunos inadimplentes" estiver desmarcado.

O comportamento de verificação de inadimplência continua o mesmo para as matriculas presenciais, via portal e processos seletivos.

A transferência interna entre coligadas deverá na avaliação de inadimplência verificar o parâmetro de tesouraria “**Verificar débitos do aluno em outras coligadas**” (Configurações | Parâmetro | Tesouraria | Geral 1/4). Exemplo: o aluno possui débitos na coligada origem e na coligada destino foi feita parametrização para não verificar débitos em outras coligadas, desta forma a transferência sempre será realizada, pois na coligada destino não existe débito para o aluno.

Quando houver uma transferência de um aluno de A (período letivo 2016/1) para B (período letivo 2016/1) e em outro momento for realizada a operação inversa o parâmetro do TOTVS Educacional a ser avaliado não mais será o "Bloquear matrícula de inadimplentes" e sim o **"Bloquear mudança de situação de matrícula para inadimplentes"** (Configurações | Parâmetro | Matricula | Movimento 1/4). O motivo da utilização do parâmetro "Bloquear mudança de situação de matrícula para inadimplentes" é que neste cenário não está sendo realizada uma matrícula e sim uma alteração de situação de matrícula.

Veja Também

---

[Documento Técnico - Verificar a inadimplência interna](http://tdn.totvs.com/display/LRM/ER_EDUEDU001-69_Verificar_Inadimplencia_Transferencia_Interna)

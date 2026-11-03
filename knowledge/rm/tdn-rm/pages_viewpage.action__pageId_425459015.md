---
content_hash: 0ffd15451e3e81bc718baba0958a2e62bff1888323970f842e760425fb980c1b
fetched_at: '2026-06-29T00:09:33.408594+00:00'
page_id: '425459015'
product: rm
source: tdn-rm
title: Inadimplência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459015
version: 4
---

---

A validação de inadimplência é feita através da pesquisa de **boletos** vencidos e em aberto. Alunos que tiverem boletos cuja data de vencimento for menor que hoje e que ainda estiverem em aberto serão considerados inadimplentes.  
   
**Atenção:**   
- A validação de inadimplência não verifica a data de vencimento do lançamento financeiro e sim do seu **boleto**. Se desejar alterar a data de vencimento do boleto, caso tenha permissão, acesse o TOTVS Gestão Financeira e execute o processo específico para esta ação (*Manutenção de Boletos|Alterar Data de Vencimento*).   
- Se a data de vencimento do lançamento financeiro de um aluno estiver vencida mas a data de vencimento do seu respectivo boleto não estiver vencida, este aluno **não** será considerado inadimplente.

Importante

Temos alguns parâmetros de tesouraria que podem influenciar na verificação de inadimplência como: número de dias de carência, valor máximo de tolerância para inadimplência e valor máximo da conta corrente de tolerância para inadimplência.   
Para mais detalhes do funcionamento desses parâmetros clique [aqui](https://tdn.totvs.com/display/LRM/Tesouraria)

No sistema existem alguns parâmetros específicos criados para controlar a realização ou não de determinados processos através da validação prévia de inadimplência do aluno. Estes parâmetros estão disponíveis no menu *Ambiente | Parâmetros | Educacional | Matrícula | Movimento 1/4*:

- Bloquear matrícula para inadimplentes   
- Bloquear matrícula apenas para inadimplentes na matriz da matrícula (*Nível Superior*)   
- Bloquear matrícula apenas para inadimplentes na mesma modalidade (*Nível Básico*)   
- Bloquear mudança de situação de matrícula para inadimplentes

Assim, se estes parâmetros de sistema estivem marcados, processos como *Matricular alunos*, *Alterar a situação de matrícula* e *Confirmação de matrícula por pagamento* não serão realizados para alunos inadimplentes.  
Lembramos ainda que outras opções disponíveis no sistema também devem ser observadas, pois irão interferir diretamente na execução de alguns processos:

- No cadastro de *Serviços*, marque a opção '*Verificar inadimplência durante o processo de matrícula*' para os serviços que desejarem esta verificação e, neste caso, estarão sujeitos também aos parâmetros citados anteriormente.

- No cadastro de *Bolsa* que possui outro sacado (Bolsa de crédito), marque a opção '*Verifica inadimplência do outro sacado*' para as bolsas que desejarem esta validação e, neste caso, estarão sujeitas também aos parâmetros citados anteriormente.

- No cadastro de *Perfil* do usuário, existem opções que sobrepõem à todos os parâmetros de sistema, assim, mesmo que o sistema esteja parametrizado para barrar a realização de determinados processos por inadimplência, certos usuários poderão receber permissão especial para sua realização. Estas opções estão disponíveis no cadastro de *Perfil | Anexos | Parâmetros Educacionais*.

**Observação:**  
Ao realizar um *Acordo* financeiro em um boleto já remetido ao banco o status do boleto permanecerá 'Em aberto' mas o status do lançamento financeiro passará para 'Baixado por Acordo' e, neste caso, este lançamento não será considerado como inadimplente.

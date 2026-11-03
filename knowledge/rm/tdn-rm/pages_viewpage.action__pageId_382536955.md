---
content_hash: d4e0861f761ccffdab1e21c3afb7fc4a10ba2ad63e4716ed4ea550e33c8652af
fetched_at: '2026-06-29T00:09:03.661078+00:00'
page_id: '382536955'
product: rm
source: tdn-rm
title: RMCTB00002_Erros J051 / K155
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382536955
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Erros na validação nos registros J051 / K155 |
| **Ambiente:** |  |
| **Passo a passo:** | **Erros apresentados na validação da ECF:**  "Conta não é analítica. Esta conta e centro de custo devem estar cadastradas no plano de contas (J050/J051) e ser analítica."  Ou  “A conta contábil constante neste registro deve existir no registro J050 como analítica e deve haver um registro J051 filho que vincula a conta contábil e centro de custo constantes neste registro a um referencial”.    **Eliminando a advertência/erro**  Este erro ocorre porque o PVA da ECF diferentemente da ECD valida todos os registros de centro de Custos.  Abaixo segue um exemplo (conta fictícia) :  Registro do Plano contábil/referencial  Veja que para a conta 1.1.01.0052 há vários registros associados com centro de custo:  |J050|01012010|01|A|4|1.1.01.0052|1.1.01|CAIXA|  |J051|1.01.C00082.01.2.0039|1.01.01.01.01|  |J051|1.01.C00091.01.2.0007|1.01.01.01.01|  |J051|1.01.C00092.02.1.0012|1.01.01.01.01|  |J051|1.01.C00092.02.2.0001|1.01.01.01.01|    Porém se observar no registro K155 existe uma linha onde que para a mesma conta não tem centro de custo preenchido:  Normalmente se refere a 1ª linha do K030 (Janeiro):  |K030|01012017|31122017|A00|   |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | K155 | 1.1.01.0052 |  | 1758776,08 | C | 0,00 | 0,00 | 1758776,08 | C |   Ou seja, o PVA da ECF valida esta inconsistência enquanto na ECD não.  Esta linha que está com o campo do centro de custo em branco pode ser por três motivos (Saldo anterior,  lançamentos anteriores ou dentro do período da escrituração sem centro de custo):  **Obs.:** Quando digo lançamentos anteriores, o sistema verifica estes lançamentos para conseguir compor o saldo inicial de 2017 (ou do período da Escrituração que está sendo enviada).  Saldo anterior, pode ser somente o saldo anterior do seu período já fechado (guardado na tabela CSALDOEXERCICIO) como também lançamentos anteriores a data de 01/01/2017 (ou do período da Escrituração que está sendo enviada).  1-      Caso seja lançamentos anteriores ou dentro do período da escrituração, deverá identifica-los e informar o centro de custo;  2-      Se for o saldo anterior do período contábil (esta data fica no rodapé do sistema ou nos parâmetros do Saldus) poderá informar um centro de custo para este saldo liberado, usando a opção de Preenchimento do Centro de Custo nas Movimentações (Regra SPED / ECF) disponível no menu: Escrituração Contábil/Ferramentas;  Este processo insere um Centro de Custo default , favor verificar se este processo lhe atenda.  Agora se desejar retirar os centros de custos (neste caso, deverá verificar se a entrega da ECF do ano anterior não foi informado centro de custo, caso não tenha sido enviado, esta solução poderá ser aplicada):  1-      Para retirar o registro e a associação do centro de custo deverá acessar o cadastro do centro de custo e desmarcar a flag de “Enviar para Sped Contábil”;  Caso tenha associação, o sistema não deixará desmarcar, precisando retirar primeiramente as associações.  Caso sejam muitas, orientamos que o DBA da empresa desmarque esta flag via BD (tabela GCCUSTO, campo ENVIASPED);  2-      após acesse o menu cadastros/paralelo/processos/ Associação Dinâmica do Centro de Custo/Conta Gerencial ao Plano Paralelo. Como não há mais centro de custo para ser enviado, este processo irá desassociar.  Favor avaliar com o setor da contabilidade qual a melhor opção.    **Obs.** Para um melhor entendimento sobre a regra de centro de custo na ECD leia a FAQ abaixo: |
| **Observações:** | Preferencialmente execute o processo acima em base de homologação primeiramente e após validar o resultado final, execute em base oficial. |

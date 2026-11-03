---
content_hash: 78b965aecfededaa992339d13efe2be8fea23b60f2fdc90c4d390ac6170c3164
fetched_at: '2026-06-29T00:10:07.334819+00:00'
page_id: '452719404'
product: rm
source: tdn-rm
title: S-2299 - Desligamento
type: documentation
url: https://tdn.totvs.com/display/LRM/S-2299+-+Desligamento
version: 2
---

São as informações destinadas a registrar o desligamento do trabalhador da empresa/órgão público de forma definitiva por algum dos motivos constantes na tabela "19 - Motivos de Desligamento".  
 **Observações:**

* No mês do desligamento, ainda que tenha ocorrido rescisão complementar, essas verbas serão discriminadas no evento S-2299.
* Caso a coligada utilize tomador de Serviços, a estrutura desse evento será criada conforme a distribuição do Sefip, ou seja, as verbas serão discriminadas de acordo com o valor rateado por tomador que terá vínculo a uma Lotação Tributária.
* Para que o evento com código de cálculo "150 – Líquido de rescisão" seja desconsiderado na geração do S-2299, o mesmo deverá ser informado em Parametrizador | eSocial | Registros Inativos no parâmetro | Eventos a desconsiderar.

**Considerações sobre algumas tag's geradas no arquivo:**  
 Grupo consigFGTS  
 A partir do layout 2.4.02 o grupo poderá retornar até no máximo 9 empréstimos consignados.   
 Observações:   
 Será considerado apenas os empréstimos:

* Cadastrados com a flag "Funcionário firmou contrato de empréstimo consignado com garantia de FGTS" marcada.
* Que possuem parcelas em aberto.
* Empréstimos mais atuais Exemplo: Caso exista dez empréstimos consignados com parcelas em aberto cadastrados para o funcionário, o sistema irá filtrar os nove mais atuais, descartando o ultimo.

Grupo sucessaoVinc  
 Em casos que o evento S-2299 tenha por origem um desligamento referente a uma transferência para outra base de dados, a tag cnpjSucessora deverá ser preenchida manualmente dentro da aba "Situação" do cadastro do funcionário.  
 Grupo infoInterm e infoTrabInterm  
 Para a correta geração das informações, dentro do cadastro de intermitente se faz necessário a vinculação de um envelope de pagamento na competência na aba "Pagamentos" para as convocações.  
 Tag qtdDiasInterm: Retorna a quantidade de dias presente na aba "Pagamentos".  
 Tag codConv: Retorna o Código da Convocação.    
 [**Mapeamento das informações do evento**](http://tdn.totvs.com/display/LRM/Evento+S-2299)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Não Periódicos

Gerar XML

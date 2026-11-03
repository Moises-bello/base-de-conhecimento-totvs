---
content_hash: fb4fcf6aadc35917299ac6c06be1dfedd4d57ce98fccb65ece68d50eca4735ee
fetched_at: '2026-06-29T00:09:36.209191+00:00'
page_id: '425459483'
product: rm
source: tdn-rm
title: Layout do Arquivo de Inscrição Anônima
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459483
version: 7
---

Este arquivo TXT deve obedecer a um layout de colunas definido pelo sistema:

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** |
| CODCOLIGADA | Código da coligada | Sim |
| IDPS | Código do processo seletivo | Sim |
| NUMEROINSCRICAO | Número da inscrição | Sim |
| NOME | Nome do candidato | Sim |
| DTNASCIMENTO | Data de nascimento do candidato (dd/mm/aaaa) | Sim |
| NATURALIDADE | Cidade natal do candidato | Sim |
| ESTADONATAL | Estado natal do candidato (MG, PR etc) | Sim |
| SEXO | Sexo do candidato (M ou F) | Sim |
| RUA | Endereço do candidato | Não |
| NUMERO | Endereço do candidato | Não |
| COMPLEMENTO | Endereço do candidato | Não |
| BAIRRO | Endereço do candidato | Não |
| CEP | Endereço do candidato | Não |
| CIDADE | Endereço do candidato | Não |
| ESTADO | Endereço do candidato (MG, PR etc) | Não |
| TELEFONE1 | Telefone residencial do candidato | Não |
| TELEFONE2 | Telefone profissional do candidato | Não |
| INSCRICAOENEM | Número de inscrição no ENEM | Não |
| ANOREFERENCIAENEM | Ano de referência no ENEM | Não |
| CARTIDENTIDADE | Número da carteira de identidade | Sim |
| ORGEMISSORIDENT | Órgão emissor da carteira de identidade | Não |
| UFCARTIDENT | Estado da carteira de identidade (MG, PR etc) | Não |
| CPF | CPF do candidato | Não |
| EMAIL | E-mail do candidato | Não |
| PRIMEIRAOPCAO | Área de interesse ofertada escolhida como primeira opção | Sim |
| SEGUNDAOPCAO | Área de interesse ofertada escolhida como segunda opção | Não |
| CODIDIOMA | Idioma escolhido na inscrição | Não |
| DEFAUDITIVA | Portador de deficiência auditiva? (T ou F) | Sim |
| DEFVISUAL | Portador de deficiência visual? (T ou F) | Sim |
| DEFFISICA | Portador de deficiência física? (T ou F) | Sim |
| DEFFALA | Portador de deficiência de fala? (T ou F) | Sim |
| DEFMENTAL | Portador de deficiência mental? (T ou F) | Sim |
| DEFINTELECTUAL | Portador de deficiência intelectual? (T ou F) | Sim |
| BRPDH | Reabilitado(BR) | Sim |
| DEFOUTRAS | Portador de outras deficiências? (T ou F) | Não |
| DEFMOTIVOOUTRAS | Descrição de outras deficiências | Não |
| ENSINOMEDIO | O candidato estará com o ensino médio concluído na data de matrícula? (T ou F) | Não |
| CODMUNICIPIO | Código do município escolhido para realização das provas | Não |
| CODETDMUNICIPIO | Código do estado onde fica o município escolhido para realização das provas (MG, PR etc) | Não |
| IDCAMPUS | Código do campus escolhido para realização das provas. | Não |
| CORRACA | Código da Cor/Raça do candidato, este campo deverá receber código referente a cor/raça, e não a descrição da mesma. Este campo poderá ser encontrado no caminho: Serviços Globais\Administração\Tabela Dinâmica\Sistema: Folha de Pagamento\IN46 - Cor\Raça | Não |

**EX de uma linha do arquivo**:  
1;59;103;Enzo Gonzales 2;01/02/1983;Belo Horizonte;MG;M;;;;;;;;;;;;12345671;;;58727418472;enzo.gonzales@instituicao.com.br;56;;;F;F;F;F;F;F;F;;;;;;;

Versões anteriores a 12.1.21 não continham os campos DEFFALA, DEFMENTAL, DEFINTELECTUAL e BRPDH, no lugar destes existia o DEFMULTIPLA.

---
content_hash: a234b358ddeba9e041edf2745b81770c169e4b14f579ad4cc4360ff6cc59f544
fetched_at: '2026-06-29T00:10:04.750319+00:00'
page_id: '452719244'
product: rm
source: tdn-rm
title: S-2200 – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719244
version: 8
---

Este evento registra a carga inicial de funcionários, admissão do empregado ou o ingresso de servidores estatutários. Trata-se do primeiro evento relativo a um determinado vínculo – excetuado a situação prevista para o evento "S-2190 -Admissão de Trabalhador-Registro Preliminar", registrando as informações cadastrais e do contrato de trabalho. Pode ocorrer também quando o empregado é transferido de uma empresa do mesmo grupo econômico ou em decorrência de uma sucessão, fusão ou incorporação.  
   
O arquivo contém informações do cadastro de Funcionários e que, também, envolve dados de Pessoa.  
   
**Considerações sobre algumas tag's geradas no arquivo:**  
tpRegimeTrab (Tipo de regime trabalhista)  
Os dados são extraídos do campo "Tipo de Funcionário" em Administração de Pessoal | Funcionários | Salário / Jornada, sendo:  
Para o tipo de funcionário "A-Autônomo" será preenchido "RJP - Regime Jurídico Próprio";  
Para o tipo de funcionário "U-Outros" será preenchido "RJU - Regime Jurídico Único";  
Para os demais tipos será preenchido "CLT - Consolidação das Leis de Trabalho".  
   
natAtividade (Tipo de Vínculo Trabalhista)  
Os dados são extraídos do campo "Tipo de Funcionário" em Administração de Pessoal | Funcionários | Salário / Jornada, sendo:  
Para o tipo de funcionário "R-Rural" será preenchido "Trabalhador Rural";  
Para os demais tipos será preenchido "Trabalhador Urbano".  
   
Endereço será informado do Brasil se o campo Nacional estiver marcado no Cadastro de Municípios do módulo de Gestão Fiscal, caso contrário será endereço do exterior.  
   
Para o Tipo de Logradouros, Países e Municípios veja regra no parametrizador do módulo de Folha de Pagamento.  
   
Informações de trabalhador estrangeiro para registro de RNE deverá ser cadastrado na pasta Documentos Estrangeiros.  
   
tpContaBancaria – é um parâmetro novo nas informações bancárias do funcionário.  
   
A Observação das informações de deficiente será a concatenação dos campos "Recursos para realização do trabalho" e "Recursos p/ acessibilidade ao local de trabalho" no cadastro de pessoas na pasta Informações Adicionais.  
   
O tipo de dependente 09 corresponde a pais então serve para Pai e para Mãe.  
   
Para as informações abaixo foram criados campos no cadastro de funcionários e os mesmo irão com default branco e para informação no arquivo será considerado que todos os funcionários serão tipo 1.  
   
tpRegimePrev – Tipo de regime previdenciário na pasta Situação  
   
indAdmissao - Indicativo de Admissão na pasta Registro  
   
O codCargo para o eSocial corresponde ao nosso código da função que é informado anteriormente no arquivo S-1030 - Tabela de Cargos.  
Observação: Esta TAG será gerada nas seguintes situações:

* Base sem integração com o Vitae,o sistema levará nesta TAG as informações cadastradas no anexo do funcionário Observações contratuais.
* Base integrada com o Vitae,o sistema irá considerar os exames admissionais ou demissionais que estiverem Aptos com a data dos eventos não periódicos posterior a obrigatoriedade cadastrada no parametrizador.As funções dos funcionários que possuem estes exames devem ter os cbos específicos (782310,782320,782405,782410,782415,782505,782510,782515).

Grupo horContratual - O grupo sempre será retornado no XML caso o "Tipo de regime da jornada (tpRegJor)" seja igual a 1, para os demais casos o mesmo será retornado apenas se todos os campos obrigatórios estiverem preenchido.  
qtdHrsSem - Média de horas semanais, considerando uma projeção de 7 dias.  
Regra do cálculo: soma das horas das jornadas de trabalho do horário, dividido pelos dias do horário (todos os índices, inclusive dias de descanso), multiplicado por 7 (fixo).  
**Exemplos:**  
Horário com 7 dias, 5 são jornadas trabalhadas, total de 40 horas: (40 / 7 \* 7) = 40hs Horário com 14 dias, 10 são jornadas trabalhadas, total de 84 horas: (84 / 14 \* 7) = 42hs Horário com 3 dias, 2 são jornadas trabalhadas, total de 16 horas: (16 / 3 \* 7) = 37hs  
Observações:

1. Caso o registro seja desconsiderado por falta de campo(s) obrigatório(s) não preenchido(s), será apresentado um aviso ao gerar o XML. Se na etapa 6 do parametrizador eSocial estiver marcado o parâmetro "**Gerar erro de preenchimento para registro não obrigatório quando tiver algum campo preenchido**", será apresentado erro ao invés de aviso.
2. Se o horário vinculado ao funcionário estiver nos parâmetros de horários a desconsiderar e o "Tipo de regime da jornada (tpRegJor)" seja diferente de 1, o grupo não será retornado no XML independe se os campos estão preenchidos.

Grupo sucessaoVinc - Será demonstrado no XML apenas quando ocorrer a transferência do funcionário entre coligadas que possuem CNPJ diferentes, para os demais casos será gerado S-2206.  
Observação: Caso seja feita a transferência do funcionário para outra coligada (CNPJ diferente) e em seguida transferido para outra filial ou coligada de mesmo CNPJ, sem que seja integrado com o TAF o S-2200 da primeira transferência, o grupo também será visualizado.

treiCap - Serão considerados na geração do evento os treinamentos com data de fechamento (campo VTUAVCONH.DTFECHAMENTO) anterior ou igual a data de admissão ou data de transferência.   
[**Mapeamento das informações do evento**](http://tdn.totvs.com/display/LRM/Evento+S-2200)

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Iniciais

Gerar XML

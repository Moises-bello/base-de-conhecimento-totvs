---
content_hash: f4addfbfe9f966c2eb37c46c48ede619a4eb7a1ea1fed7fd9750ef346bfa7954
fetched_at: '2026-06-29T00:10:08.850617+00:00'
page_id: '452719594'
product: rm
source: tdn-rm
title: S-2100 - Evento Cadastramento Inicial de Vínculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719594
version: 2
---

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
    
 O tipo de dependente 08 corresponde a pais então serve para Pai e para Mãe.  
    
 Para as informações abaixo foram criados campos no cadastro de funcionários e os mesmo irão com default branco e para informação no arquivo será considerado que todos os funcionários serão tipo 1.  
    
 tpRegimePrev – Tipo de regime previdenciário na pasta Situação  
    
 indAdmissao - Indicativo de Admissão na pasta Registro  
    
 O codCargo para o eSocial corresponde ao nosso código da função que é informado anteriormente no arquivo S-1030 - Tabela de Cargos.  
    
 **Atenção:**  
 -Funcionário em situação de Férias (Status F)  
 -Período de gozo atual devem estar com situação Pagas.  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Eventos Iniciais

Gerar XML

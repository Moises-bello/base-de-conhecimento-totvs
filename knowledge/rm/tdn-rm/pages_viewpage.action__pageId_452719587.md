---
content_hash: 6037aced77852adf649752e784620ca20a0bee4e3b792848e4755d91234549c1
fetched_at: '2026-06-29T00:10:08.822453+00:00'
page_id: '452719587'
product: rm
source: tdn-rm
title: Admissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719587
version: 2
---

Etapa utilizada para configurar algumas validações no processo de admissão do funcionário  
    
 **Parâmetros**  
 Consiste Duplicidade de CPF  
 Com este parâmetro marcado é feito uma validação no CPF informado no cadastro de funcionário. Caso exista alguma pessoa com o mesmo CPF, é retornado a mensagem abaixo:  
 "Já existe na base uma ou mais pessoas com este CPF cadastrado, favor confirmar se não se trata da mesma pessoa. Caso seja a mesma pessoa, verifique a possibilidade de utilizar os dados desta pessoa. Confirma o cadastramento?"  
    
 Consiste Duplicidade de PIS  
 Com este parâmetro marcado é feito uma validação no PIS informado no cadastro de funcionário. Caso exista algum funcionário com o mesmo PIS, é retornado a mensagem de confirmação conforme abaixo:  
 "Já existe funcionário cadastrado com este PIS/PASEP! Confirma o cadastramento?"  
    
    
 Consiste Duplicidade de  CTPS  
 Com este parâmetro marcado é feito uma validação na CTPS informada no cadastro de funcionário. Caso exista algum funcionário com a mesma CTPS, é retornado a mensagem abaixo:  
 "Já existe funcionário cadastrado com este CTPS! Confirma o cadastramento?"  
    
 **Observação**  
 Caso o usuário opte por não duplicar estes campos, o sistema não salvará as alterações. Caso contrário, mesmo fazendo as validações de duplicidade de CPF, PIS e CTPS, o cadastro do funcionário é finalizado com sucesso.  
    
 Somente Inclui funcionários em processo de Admissão no RM Vitae  
 Com este parâmetro marcado, o sistema só permitirá a inclusão de funcionários utilizando o quadro de candidatos que se encontram em processo de admissão pelo TOTVS Gestão de Pessoas. Quando o usuário for incluir um novo funcionário, será aberto um quadro com todos os candidatos que se encontram em processo de admissão e seleção no TOTVS Gestão de Pessoas. Ao escolher o candidato a ser admitido, os dados deste serão resgatados para o TOTVS Folha de Pagamento com seus respectivos dados pessoais. Para Finalizar a inclusão de um novo funcionário, o usuário deverá completar o cadastramento do mesmo, com as informações necessárias a sua admissão.

**Observação**  
 Este campo só está disponível se a base estiver parametrizada para integrar com Módulo TOTVS Gestão de Pessoas  
 Copiar informações dos dependentes do funcionário  
 Com este parâmetro marcado, na inclusão do funcionário, ao clicar em 'Salvar' ou 'OK', a cópia dos dados dos dependentes existentes será automática sem questionamentos ao usuário.  
 Com este parâmetro desmarcado, na inclusão do funcionário, ao clicar em 'Salvar' ou 'OK', o usuário receberá uma mensagem questionando-o sobre a cópia ou não dos dados dos dependentes, caso os mesmos existam.  
    
 Data de Admissão igual ao primeiro dia da Competência Atual  
 Com este parâmetro marcado, o campo Data da Admissão retorna preenchido com o primeiro dia da competência da base. Com este parâmetro desmarcado, o campo Data de Admissão retorna em branco.

**Observação**  
 Mesmo que tenha valor default configurado para o campo Data de Admissão, com o parâmetro marcado sempre retorna o primeiro dia do mês da competência da base.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<< Retornar para **Folha de Pagamento**

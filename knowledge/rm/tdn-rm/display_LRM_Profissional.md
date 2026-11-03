---
content_hash: e5d01e60979f65861ff8f794e5623b7cc8c0672c8919304f4a3766a83bb95c12
fetched_at: '2026-06-29T00:09:30.831063+00:00'
page_id: '425458543'
product: rm
source: tdn-rm
title: Profissional
type: documentation
url: https://tdn.totvs.com/display/LRM/Profissional
version: 3
---

A tabela auxiliar "Profissional" é o "banco" de profissionais que a instituição irá manter para utilizar nos seus processos seletivos. Nesse cadastro a instituição poderá incluir funcionários ou fornecedores terceirizados.   
 Funcionários são as pessoas que já trabalham na instituição, as que constam no Cadastro de Funcionários e poderão trabalhar nos processos seletivos. Os Clientes/Fornecedores podem ser alunos, empresas, pessoas da comunidade ou qualquer outra que não seja funcionário e que conste no Cadastro de Cliente/Fornecedor da instituição.  
 O usuário não está limitado a incluir apenas Clientes/Fornecedores que já existam no Cadastro de Clientes/Fornecedor, mas também poderá acrescentar novos registros.

* Importante A tela "Profissional" será controlada por filial quando acessada pelo TOTVS Educacional.

O controle de profissionais por filial irá ocorrer somente para os profissionais extraídos da tabela PFUNC. Para os funcionários criados fora da tabela PFUNC o controle de filial não será utilizado. Com este controle de filial o processo de Alocar profissionais ganhou um novo parâmetro quando acessado pelo TOTVS Educacional que será possível alocar profissionais de outra filial caso não tenha profissionais suficientes cadastrados na filial onde está ocorrendo a alocação.  
 O campo "Ativo?" será utilizado pelo usuário para informar ao sistema se aquele profissional estará temporariamente ou permanentemente indisponível para trabalhar nos processos seletivos. Dessa maneira, os profissionais inativos não serão considerados nos processos do processo seletivo.  
    
 O campo "Sexo" será preenchido automaticamente quando o profissional for um funcionário e não será possível alterar seu valor. No caso de Cliente/Fornecedor esse campo estará habilitado para preenchimento. O preenchimento será opcional. Quando o valor para o campo sexo não for informado, o profissional apenas será alocado automaticamente em locais que permitam alocação de ambos os sexos.  
 Durante o cadastro de um profissional o seu perfil também deverá ser configurado, informando um ou mais "tipo de profissional" para ele.

**Utilizações importantes**:  
 O Processo "Alocar Profissionais em Locais do Processo Seletivo" será executado para um processo seletivo no intuito de definir os profissionais que trabalharão nos locais disponibilizados. Esse processo baseia-se nas informações de perfis e quantidades de profissionais definidos previamente no cadastro de locais disponíveis em um processo seletivo.   
 No Cadastro "Processo Seletivo" será possível visualizar todos os profissionais que foram alocados para trabalhar nele após a execução do processo Alocar Profissionais em Locais do Processo Seletivo.   
 Será possível também remanejar individualmente os profissionais, realocando-os conforme a necessidade e alocar manualmente um profissional em um local específico.

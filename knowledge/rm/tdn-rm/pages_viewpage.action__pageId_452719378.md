---
content_hash: 7d613da1b81490a5dc8f18678f3ccebc79b7eb9506e0c9cf0cfc7095f3fa2edf
fetched_at: '2026-06-29T00:10:07.230191+00:00'
page_id: '452719378'
product: rm
source: tdn-rm
title: Adequações do TOTVS Automação de ponto à Portaria 1510/2009
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719378
version: 3
---

**Adequações do TOTVS** **Automação de ponto** **à Portaria 1510/2009**

A Portaria 1510/2009 disciplina o registro eletrônico de ponto e a utilização do Sistema de Registro Eletrônico de Ponto – SREP. O SREP deve registrar fielmente as marcações efetuadas, não sendo permitida qualquer ação que desvirtue os fins legais a que se destina. Nessa Portaria, o TOTVS Automação de ponto se enquadra como "Programa de Tratamento de Registro de Ponto" e atende a portaria gerando os relatórios legais (AFDT, ACJEF, Espelho de Cartão de Ponto da Portaria) e não permite, de forma alguma, a perda de informações das batidas originais e garante a manutenção de informações sobre as batidas incluídas.

**OBSERVAÇÃO**

Todos os termos utilizados no TDN referentes à exclusão, alteração ou cancelamento de batidas de funcionários dizem respeito às batidas consideradas no cálculo, mantendo a Memória de registro de ponto das batidas originais, onde os dados armazenados não podem ser apagados ou alterados, como um meio de armazenamento permanente.

Todas as batidas iguais ou posteriores a data 01/11/2009, originais ou incluídas, são armazenadas em banco de dados utilizando técnica de validação por CRC. CRC é um cálculo matemático (uma função hash) normalmente utilizado para detectar corrupções de dados / programas, com a intenção de manter a integridade das batidas.

Manipulação de batidas por fora do sistema, alterações na base de dados ou sistemas de terceiros, invalidará o CRC e os relatórios legais não serão gerados informando um código de erro que permitirá identificar quais os registros foram modificados.

Usuários do sistema poderão consultar a qualquer momento estes registros através dos relatórios apropriados (AFDT e Espelho de Cartão da Portaria) ou até mesmo examinando a base de dados.  
Vale ressaltar ainda que adequação à Portaria 1510/2009 não se limita a instalação da versão do RM Chronus 10.80.0. É necessário um completo entendimento dessa portaria que pode ser acessada no site do Ministério do Trabalho e Emprego: <http://www.mte.gov.br/>

Várias alterações demandam adequações no processo de utilização do ponto eletrônico do cliente - software, dispositivos e processos. Citando algumas:

(...)

Art. 2º O SREP deve registrar fielmente as marcações efetuadas, não sendo permitida qualquer ação que desvirtue os fins legais a que se destinam, tais como:

I - restrições de horário à marcação do ponto;

(...)

O cliente não poderá restringir horários de marcação de ponto. Este tipo de funcionalidade é de utilização comum para clientes que utilizam softwares de terceiro para controle de acesso.

Ainda neste artigo:

(...)

III - exigência, por parte do sistema, de autorização prévia para marcação de sobrejornada;

(...)

É necessário que o cliente pare de autorizar extras parcialmente e parametrize as horas extras para ficarem sempre autorizadas.

Em suma, a Portaria 1510/2009 altera significativamente a forma de utilização de ponto eletrônico pelas empresas e nossos clientes precisam adequar não somente nosso software, como outros dispositivos e seus processos.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Relatório AFDT  
Espelho(Portaria 1510/2009)  
   
HelpWiki - RH - Automação de Ponto

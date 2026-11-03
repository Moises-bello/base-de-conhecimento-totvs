---
content_hash: c1882f1439095eca46745383cbfed5a159eb9cfd1d5cc568f8a35c2c3e9e4a0f
fetched_at: '2026-06-29T00:06:00.202251+00:00'
page_id: '195299965'
product: rm
source: tdn-rm
title: RMFIS00013_05 - Apuração Virtual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=195299965
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.38 e superiores** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 27/07/2015 |

Para empresas com apurações trimestrais do IRPJ e CSLL, a ECF exige que as informações do Bloco K sejam enviadas com os valores de **Ativo e Passivo fechados**. Porém, de acordo com a Lei nº 6.404/1976, art. 175 e Lei nº 9.430/1996, arts. 1º e 2º, para fins societários, o exercício social permanece com duração de 1 ano, encerrando-se, normalmente, em 31 de dezembro.

Embora caiba à pessoa jurídica adotar procedimentos que permitam ao Fisco constatar a veracidade do resultado apurado, a elaboração de balanços/balancetes trimestrais não representa obrigatoriedade de encerramento das Contas de Resultado a cada trimestre.

Para atender as necessidades de apuração trimestral, sem que se faça necessário o encerramento das contas contábeis, disponibilizamos o módulo de **Apuração Virtual** que possibilita criar estruturas de apuração contábil (ou de apoio gerencial) que serão processadas no momento da geração do arquivo da ECF, **não gerando nenhum impacto na escrituração contábil do sistema**.

**Para acessar: Nova MDI | Gestão Contábil - Escrituração Contábil | Apuração Virtual.**

Para cada período a ser processado o sistema utilizará o molde da Apuração Virtual informado para compor o saldo da conta de lucro ou prejuízo que será gerado no registro K155, posteriormente será possível realizar a conferência dos valores da apuração em seus detalhamentos.

As empresas com apuração pelo lucro real anual, podem, opcionalmente, utilizar o procedimento acima.

**Orientações importantes!**

1. Na versão 11.82 e 11.82, para que o campo "**Conta de Prejuízo**" apresentado no print acima seja apresentado é preciso executar script. Solicite-o ao Suporte.
2. As contas parametrizadas para Lucro e Prejuízo **devem ser as mesmas que foram parametrizadas na Transferência de Grupos Contábeis** para o encerramento anual. No caso de serem diferentes, ocasionará diferença no fechamento do Balancete na ECF.

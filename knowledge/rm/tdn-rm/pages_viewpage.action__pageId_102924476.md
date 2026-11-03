---
content_hash: b3d9b8645401ed6571482729f0ce3ce5d0b6f5213bbb897d7ea26d2f2b85ce65
fetched_at: '2026-06-29T00:05:48.842491+00:00'
page_id: '102924476'
product: rm
source: tdn-rm
title: RMFIS00018_Diferencial de Alíquota
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=102924476
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:**11.52 |
| **Processo** | **:** | SPED Fiscal - Diferencial de Alíquota |
| **Subprocesso** | **:** | Apuração de ICMS com diferencial |
| **Data da publicação** | **:** | 17/09/2013 |

**Introdução:**

Para que o valor do diferencial de alíquota que não afeta a Apuração do ICMS, mas tem uma guia gerada no período de apuração seja gerado no PVA, é necessário gerar os Registros C197/C195, referentes a ajuste que serão somados diretamente na Apuração no Registro E110 Campo 15-DEB\_ESP valores recolhidos ou a recolher extra-apuração.   
  
 Para geração dos valores Extra Apuração, deverá ser criado alguns campos complementares para geração dos registros C195/C197.   
  
 Lançamentos de Diferencial de alíquota requer que o tipo do ICMS definido no cadastro da natureza fiscal de operação, utilizada nos lançamentos, seja de Diferencial de alíquota e para atender a rotina, deve-se criar os campos complementares (Código ajuste, descrição e valor) e preenche-los devidamente (conforme orientação do guia prático do SPED). O lançamento deve conter itens e nos itens, informar também o valor do Diferencial de Alíquota.   
  
 Aos valores de Outros Débitos/Créditos, serão consistidos os lançamentos com a informação do Código Ajuste do SPED (Menu Lançamentos – Outros Débitos/Créditos).   
  
 Os códigos de Ajuste do SPED FISCAL são fornecidos pela própria [Receita Federal](http://www1.receita.fazenda.gov.br/sistemas/sped-fiscal/tabelas-de-codigos.htm)

* + **Campos Complementares:**  
      
      
     Os campos complementares são criados no aplicativo RM LIBER pelo menu **Cadastros | Campos Complementares**. Se a empresa trabalha com o RM Nucleus, os campos também devem ser criados neste aplicativo, da mesma forma, para que ao escriturar os movimentos a informação vá preenchida para o aplicativo fiscal.   
      
    **OBS: SE O LANÇAMENTO FOR REFERENTE A NF-E (NOTA FISCAL ELETRÔNICA) E DE EMISSÃO PRÓPRIA, MODELO 55, OS CAMPOS COMPLEMENTARES DEVEM SER CRIADOS, NA OPÇÃO LANÇAMENTO FISCAL.**  
    **DEMAIS SITUAÇÕES, CRIAR NO ITEM DO LANÇAMENTO FISCAL.**

* + Em vermelho, refere ao campo "nome da Coluna". O que preencher no campo Descrição; fica a critério do usuário.

* + **CODAJUSTESPED** **(alfanumérico, tamanho - 10)** – Código de ajuste de acordo com a tabela 5.3 (10 caracteres) para geração correta dos registros C195/C197;

* + **DESCAJUSTESPED** **(texto)** – Descrição complementar do ajuste de apuração (registro C197).

* + **VALORICMSAJUSTE****(real)** – Valor que deverá ser tratado como ajuste, referente ao diferencial de alíquota , para que seja gerado o Registro C197.

**Exemplo**:

**Informações Adicionais:**

* + Como utilizar o Código de Ajuste?
  + Quando utilizar 8 ou 10 dígitos?
  + O que o código de ajuste quer dizer?

Para utilizar o código de ajuste, primeiro é necessário verificar como esta parametrizado a apuração para Diferencial de Alíquota nos parâmetros do sistema. Acesse o menu **Opções – Parâmetros – Gerais/Tabelas – Apuração de tributos – ICMS – etapa Apur. ICMS por filial** – seleciona a filial e dê duplo clique  sobre a filial – campo Resumo de apuração.

* + Se a opção estiver desmarcada, sempre que houver lançamento de diferencial de Alíquota o Cliente tem que, dentro do item, informar o código de ajuste de acordo com a tabela do ESTADO, neste caso de 10 dígitos:

**Lembre-se:**

Para o parâmetro desmarcado os códigos devem ser com 10 Dígitos. **Exemplo Tabela 5.3:**

**Conteúdo da tabela: 5.3 - Tabela de Ajustes e Informações de Valores Provenientes de Documento Fiscal – exemplo Estado RJ.**

Veja que no período de apuração teve um valor de crédito e também um valor de diferencial  de alíquota de R$ 60,00.

Em uma possível situação, de que se o Cliente gerar a guia no período de apuração e não informar o código de ajuste do SPED, o PVA vai consistir a seguinte crítica: O somatório dos campos 'Valor da obrigação a recolher' dos  registros E116 exibido na coluna  'Valor  Calculado', não é igual  à soma  dos campos 'Valor total  de ICMS a recolher' e 'Valores recolhidos ou a recolher extra-apuração' do registro E110:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C100 | 0 | 1 | GF06666 | 01 | 00 | 1 | 111111 | 25012012 | 25012012 | 1000,00 | 9 | 0 | 0 | 1000,00 | 9 | 0 | 0 | 0 | 1000,00 | 120,00 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C170 | 1 | 01.01 | 1,00000 | UN | 1000,00 | 0 | 0 | 000 | 2101 | 2.101.01 | 1000,00 | 12,00 | 120,00 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C190 | 000 | 2101 | 12,00 | 1000,00 | 1000,00 | 120,00 | 0 | 0 | 0 | 0 |
| E100 | 01012012 | 31012012 |
| E110 | 0 | 0 | 0 | 0 | 120,00 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 120,00 | **0** |
| E116 | 60,00 | 01012012 | 104 0 | 012012 |

**Qual seria o motivo desta crítica?** Veja que no campo 13 do registro E110 não existe informação de Débito nem no campo 15 (Do diferencial), mas foi gerado uma guia (E116) com valor de R$60,00.

**Como resolver?** Acesse o lançamento de DA (Dif. de alíquota) e informe o código de ajuste no item

Este valor vai entrar como Extra Apuração (campo 15 do E110)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C100 | 0 | 1 | GF06666 | 01 | 00 | 1 | 111111 |  | 25012012 | 25012012 | 1000,00 | 9 | 0 | 0 | 1000,00 | 9 | 0 | 0 | 0 | 1000,00 | 120,00 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C170 | 1 | 01.01 |  | 1,00000 | UN | 1000,00 | 0 | 0 | 000 | 2101 | 2.101.01 | 1000,00 | 12,00 | 120,00 | 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 | 0 |  | 0 | 0 | 0 | 0 | 0 |  |

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C190 | 000 | 2101 | 12,00 | 1000,00 | 1000,00 | 120,00 | 0 | 0 | 0 | 0 |

|  |  |  |
| --- | --- | --- |
| C195 | 1 |  |

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C197 | RJ70000002 | Ajuste RJ | 01.01 | 1000,00 | 0 | 60,00 | 0 |

|  |  |  |  |
| --- | --- | --- | --- |
| E100 | 01012012 | 31012012 |  |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E110 | 0 | 0 | 0 | 0 | 120,00 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 120,00 | 60,00 |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E116 |  | 60,00 | 01012012 | 104 0 |  |  |  |  | 012012 |

---

* + Se a opção estiver habilitado: Será consistido os lançamentos de outros débitos/créditos.

Caso ocorra o erro a seguir, verifique:

No arquivo:

|  |  |  |
| --- | --- | --- |
| E100 | 01122013 | 31122013 |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E110 | 900,00 | 0 | 0 | 0 | 240,00 | 0 | 0 | 0 | 0 | 660,00 | 0 | 660,00 | 0 | 0 |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E116 |  | 780,00 | 01122013 | 104 0 |  |  |  |  | 122013 |

**Exemplo:** Utilização da Tabela 5.1.1:

Como o Diferencial afeta a  apuração, o código deve ser de 8 dígitos e referente a Outros Débitos não Débitos Especiais como no exemplo acima:

No saldo credor/devedor do período de apuração o valor de R$ 780,00 será apresentado.

Informando o Código correto, o registro será gerado normalmente:

|  |  |
| --- | --- |
| E001 | 0 |

|  |  |  |
| --- | --- | --- |
| E100 | 01122013 | 31122013 |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E110 | 900,00 | 0 | 120,00 | 0 | 240,00 | 0 | 0 | 0 | 0 | 780,00 | 0 | 780,00 | 0 | 0 |

|  |  |  |  |
| --- | --- | --- | --- |
| E111 | MG009999 | Diferencial de aliquota MG | 120,00 |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E113 | C00022 | 01 | 1 | 0 | 222222 | 01122013 | 01.04 | 120,00 |

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E116 |  | 780,00 | 01122013 | 104 0 |  |  |  |  | 122013 |

**Exceção: LANÇAMENTOS FISCAIS DE TRANSPORTE SEMPRE DEVE SER CODIGO DE AJUSTE DE 8 DIGITOS.**

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/_layouts/searchresults.aspx?k=diferencial%20de%20al%C3%ADquota&u=http%3A%2F%2Fwikihelp%2Etotvs%2Ecom%2Ebr%2FWikiHelp)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)

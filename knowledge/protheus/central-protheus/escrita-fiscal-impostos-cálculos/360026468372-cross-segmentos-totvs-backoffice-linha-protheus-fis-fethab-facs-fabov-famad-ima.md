---
article_id: 360026468372
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 94f9fe07a6a84051ac1e24d6f0cc7d794d22322a721b0a99fd265e3e1d258138
fetched_at: '2026-06-28T22:39:31.020817+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- FETHAB, FACS, FABOV,
  FAMAD, IMA e FASE MT
type: support-article
updated_at: '2021-07-29T13:12:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026468372-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FETHAB-FACS-FABOV-FAMAD-IMA-e-FASE-MT
---

**Dúvida**Quais os procedimentos de configuração e cálculo dos impostos FETHAB, FACS, FABOV, FAMAD, IMA e FASE MT.  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Disponível o cálculo da contribuição **Fundo Estadual de Transporte e Habitação (FETHAB)**, **Fundo de Apoio a Cultura da Soja (FACS),** **Fundo de Apoio ao Desenvolvimento da Bovinocultura (FABOV)** , **Fundo de Apoio a Madeira (FAMAD) e IMA-MT**do Estado do Mato Grosso.

* **Fundo Estadual de Transporte e Habitação (FETHAB)**

É a contribuição destinada a financiar o planejamento, a execução, o acompanhamento e avaliação de obras e serviços de transportes e habitação em todo o território mato-grossense.

* **Fundo de Apoio a Cultura da Soja (FACS)**

É a contribuição destinada a financiar ações voltadas ao apoio e desenvolvimento da cultura de soja e organização do respectivo sistema de produção, por meio de entidades representativas do referido segmento.

* **Fundo de Apoio ao Desenvolvimento da Bovinocultura (FABOV)**

É a contribuição destinada a financiar as ações voltadas a apoio e desenvolvimento da bovinocultura de corte e organização do respectivo sistema de produção, por meio de entidades representativas do referido segmento.

* **Fundo de Apoio a Madeira (FAMAD).**

 É a contribuição destinada a financiar ações voltadas ao apoio e desenvolvimento do setor de base florestal e organização do respectivo sistema de produção, por meio de entidades representativas deste segmento.

* **Instituto matograssense do Algodão (IMA)**

O Instituto Mato-Grossense do Algodão (IMAmt) foi criado em 2007 com o objetivo de atender às demandas dos associados da AMPA, realizando pesquisa, desenvolvimento e difusão de novas tecnologias para os produtores.

**Dicionários**

No **Configurador** (SIGACFG) acesse **Base de Dados/Dicionário/Base de Dados**, verifique os campos/parâmetros indicados a seguir e crie-os caso não existam:

* Tabela **SB1 –****Cadastro de Produtos**

|  |  |
| --- | --- |
| **Campo** | B1\_AFETHAB |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Cabeçalho** | Alíq. FETHAB |
| **Descrição** | Alíquota FETHAB |
| ***Help*** | Alíquota FETHAB |

|  |  |
| --- | --- |
| **Campo** | B1\_AFACS |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Cabeçalho** | Aliq. FACS |
| **Descrição** | Alíquota FACS |
| ***Help*** | Valor da alíquota FACS. |

|  |  |
| --- | --- |
| **Campo** | B1\_AFABOV |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Cabeçalho** | Aliq. FABOV |
| **Definição** | Alíquota FABOV |
| ***Help*** | Valor da alíquota FABOV. |

|  |  |
| --- | --- |
| **Campo** | B1\_AFAMAD |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Cabeçalho** | Aliq. FAMAD |
| **Descrição** | Aliquota FAMAD |
| ***Help*** | Alíquota FAMAD |

|  |  |
| --- | --- |
| **Campo** | B1\_TFETHAB |
| **Tipo** | Caractere |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Tipo FETHAB |
| **Definição** | Tipo FETHAB |
| ***Help*** | Caso a tipo fethab seja 1 - Soja ou  2 - Algodao, o calculo do tributo sera em tonelada, caso seja  3 - Gado, o calculo do tributo será em unidade,caso seja  4-Madeira, o cálculo do tributo será em Metros Cubicos |
| **Lista de Opções** | 1=Soja;2=Algodao;3=Gado;4=Madeira |

Importante

Este campo é utilizado para definir se o cálculo do FETHAB será feito em tonelada, unidade ou Metros Cúbicos. Este campo só deve ser preenchido para o cálculo do FETHAB.

|  |  |
| --- | --- |
| **Campo** | B1\_AIMAMT |
| **Tipo** | B1\_AIMAMT |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Cabeçalho** | Aliq. IMA-MT |
| **Definição** | Aliquota IMA-MT |
| ***Help*** | Alíquota para cálculo do IMA-MT. (Instituto Mato-grossense do Algodão). |

* Tabela **SA1 –****Cadastro de Clientes**

|  |  |
| --- | --- |
| **Campo** | A1\_RECFET |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. FETHAB |
| **Definição** | Recolhe FETHAB |
| ***Help*** | Indica se o cliente recolhe o FETHAB.  Se recolher deverá ser preenchido com “S”, caso contrário deverá ser preenchido com “N” ou branco. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | A1\_RFABOV |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. FABOV |
| **Definição** | Recolhe FABOV |
| ***Help*** | Indica se o cliente recolhe o FABOV.  Se recolher deverá ser preenchido com “S”, caso contrário deverá ser preenchido com ”N” ou branco. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | A1\_RECFMD |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. FAMAD |
| **Definição** | Recolhe FAMAD |
| ***Help*** | Indica se o cliente recolhe o FAMAD. Se recolher deverá ser preenchido com S caso contrário deverá ser preenchido  com N ou branco. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | A1\_RIMAMT |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. IMA-MT |
| **Definição** | Recolhe IMA-MT |
| ***Help*** | Indica se o cliente recolhe o IMA-MT. |
| **Lista de Opções** | 1=Sim; 2=Não |

* Tabela **SA2 –****Cadastro de Fornecedor**

|  |  |
| --- | --- |
| **Campo** | A2\_RECFET |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. FETHAB |
| **Definição** | Recolhe FETHAB |
| ***Help*** | Informa se o fornecedor é responsável pelo recolhimento do FETHAB. Caso não seja o responsável, o Sistema fará a retenção do tributo. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | A2\_RFABOV |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. FABOV |
| **Definição** | Recolhe FABOV |
| ***Help*** | Informa se o fornecedor é responsável pelo recolhimento do FABOV. Caso não seja o responsável, o Sistema fará a retenção do tributo. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | A2\_RFACS |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. FACS |
| **Definição** | Recolhe FACS |
| ***Help*** | Informa se o fornecedor é responsável pelo recolhimento do FACS. Caso não seja o responsável, o Sistema fará a retenção do tributo. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | A2\_RECFMD |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. IMA-MT |
| **Definição** | Recolhe IMA-MT |
| ***Help*** | Informa se o fornecedor é responsável pelo recolhimento do IMA-MT. Caso não seja o responsável, o sistema fara a  retenção do tributo. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | A2\_RIMAMT |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Rec. FAMAD |
| **Definição** | Recolhe FAMAD |
| ***Help*** | Indica se o fornec recolhe o FAMAD. Se recolher deverá ser preenchido com S caso contrário deverá ser preenccido  Com N ou branco. |
| **Lista de Opções** | 1=Sim; 2=Não |

* Tabela **SF4 - Tipos de Entrada e Saida**

|  |  |
| --- | --- |
| **Campo** | F4\_CALCFET |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Calc. FETHAB |
| **Definição** | Calcula FETHAB |
| ***Help*** | Indica se para este TES haverá o calculo do FETHAB, conforme decreto 1.261/2000. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | F4\_CFACS |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Calc. FACS |
| **Definição** | Calcula FACS |
| ***Help*** | Indica se para este TES haverá o calculo do FACS, conforme decreto 1.261/2000. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | F4\_CFABOV |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Calc. FABOV |
| **Definição** | Calcula FABOV |
| ***Help*** | Indica se para este TES haverá o calculo do FABOV, conforme decreto 1.261/2000. |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | F4\_RFETALG |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Ret.Fethab |
| **Definição** | Retém FETHAB Algodão |
| ***Help*** | Indica se haverá retenção do FETHAB por parte do cliente na operação de saída, quando houver operação com algodão. |
| **Lista de Opções** | 1=Sim; 2=Não |

Importante

Para operação de saída de algodão com cálculo do FETHAB, o campo F4\_RFETALG terá maior prioridade que o campo A1\_RECFET para indicar se o cliente irá ou não recolher o valor do FETHAB. O campo F4\_RFETALG somente deverá ser preenchido nas situações onde o mesmo cliente em determinadas operações recolhe o FETHAB, e outras não recolhe, nestas situações o controle deverá ser realizado através do cadastro de TES, caso contrário deverá ser feito somente com campo A1\_RECFET. Lembrando que este campo somente irá influenciar cálculo do FETHAB com algodão.

A configuração deste campo será válida somente na situação onde o valor do título de FETHAB for gerado separadamente dos títulos de FABOV e FACS ( situação onde o parâmetro MV\_AGFETHA está com conteúdo igual a .F.), caso os valor de FETHAB, FABOV e FACS sejam agrupados no mesmo título (MV\_AGFETHA está com conteúdo igual a .T.), a configuração deste campo não será considerada.

|  |  |
| --- | --- |
| **Campo** | F4\_CFAMAD |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Calc. Famad |
| **Definição** | Calcula Famad |
| ***Help*** | Indica se para esse TES haverá o calculo do Famad – Fundo de Apoio a Madeira |
| **Lista de Opções** | 1=Sim; 2=Não |

|  |  |
| --- | --- |
| **Campo** | F4\_CIMAMT |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Validação** | Pertence(" 12") |
| **Cabeçalho** | Calc. IMA-MT |
| **Definição** | Calcula IMA-MT |
| ***Help*** | Indica se para este TES haverá o cálculodo IMA-MT (Instituto Mato-grossense) |
| **Lista de Opções** | 1=Sim; 2=Não |

* Tabela **SF1 – Cabeçalho das NF de Entrada**

|  |  |
| --- | --- |
| **Campo** | F1\_VALFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFET","MT100",M->F1\_VALFET) |
| **Cabeçalho** | Vl.FETHAB |
| **Definição** | Valor do FETHAB |
| ***Help*** | Valor calculado na operação referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | F1\_VALFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFAB","MT100",M->F1\_VALFAB) |
| **Cabeçalho** | Vl.FABOV |
| **Definição** | Valor do FABOV |
| ***Help*** | Valor calculado na operação referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | F1\_VALFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFAC","MT100",M->F1\_VALFAC) |
| **Cabeçalho** | Vl.FACS |
| **Definição** | Valor do FACS |
| ***Help*** | Valor calculado na operação referente ao FACS |

|  |  |
| --- | --- |
| **Campo** | F1\_VALFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFMD","MT100",M->F1\_VALFMD) |
| **Cabeçalho** | Vl.Famad |
| **Definição** | Valor Famad |
| ***Help*** | Valor Famad – Fundo de Apoio a madeira |

* Tabela **SD1 – Itens das NF de Entrada**

|  |  |
| --- | --- |
| **Campo** | D1\_BASEFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFET","MT100",M->D1\_BASEFET) |
| **Cabeçalho** | Base FETHAB |
| **Definição** | Base do FETHAB |
| ***Help*** | Base calculada no item referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | D1\_BASEFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFAB","MT100",M->D1\_BASEFAB) |
| **Cabeçalho** | Base FABOV |
| **Definição** | Base do FABOV |
| ***Help*** | Base calculada no item referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | D1\_BASEFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFAC","MT100",M->D1\_BASEFAC) |
| **Cabeçalho** | Base FACS |
| **Definição** | Base do FACS |
| ***Help*** | Base calculada no item referente ao FACS. |

|  |  |
| --- | --- |
| **Campo** | D1\_ALIQFET |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALIQFET","MT100",M->D1\_ALIQFET) |
| **Cabeçalho** | Aliq. FETHAB |
| **Descrição** | Alíquota do FETHAB |
| ***Help*** | Alíquota calculada do item referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | D1\_ALIQFAB |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALIQFAB","MT100",M->D1\_ALIQFAB) |
| **Cabeçalho** | Aliq. FABOV |
| **Descrição** | Alíquota do FABOV |
| ***Help*** | Alíquota calculada do item referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | D1\_ALIQFAC |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALIQFAC","MT100",M->D1\_ALIQFAC) |
| **Cabeçalho** | Aliq. FACS |
| **Descrição** | Alíquota do FACS |
| ***Help*** | Alíquota calculada do item referente ao FACS. |

|  |  |
| --- | --- |
| **Campo** | D1\_VALFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFET","MT100",M->D1\_VALFET) |
| **Cabeçalho** | Vlr. FETHAB |
| **Descrição** | Valor do FETHAB |
| ***Help*** | Valor calculado do item referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | D1\_VALFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFAB","MT100",M->D1\_VALFAB) |
| **Cabeçalho** | Vlr. FABOV |
| **Descrição** | Valor do FABOV |
| ***Help*** | Valor calculado do item referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | D1\_VALFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFAC","MT100",M->D1\_VALFAC) |
| **Cabeçalho** | Vlr. FACS |
| **Descrição** | Valor do FACS |
| ***Help*** | Valor calculado do item referente ao FACS. |

|  |  |
| --- | --- |
| **Campo** | D1\_BASEFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFMD","MT100",M->D1\_BASEFMD) |
| **Cabeçalho** | Base do Famad |
| **Definição** | Base Famad – Fundo de Apoio a Madeira |
| ***Help*** | Base calculada no item referente ao Famad |
| ***Campo*** | D1\_ALQFMD |
| ***Tipo*** | Numérico |
| ***Tamanho*** | 5 |
| ***Decimal*** | 2 |
| ***Formato*** | @E 99.99 |
| ***Validação*** | MaFisRef("IT\_ALQFMD","MT100",M->D1\_ALQFMD) |
| ***Cabeçalho*** | Aliq. Famad |
| ***Definição*** | Alíquota do Famad |
| ***Help*** | Alíquota Famad- Fundo de Apoio a Madeira |

|  |  |
| --- | --- |
| **Campo** | D1\_VALFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFMD","MT100",M->D1\_VALFMD) |
| **Cabeçalho** | Vlr. Famad |
| **Definição** | Valor do Famad |
| ***Help*** | Valor Famad – Fundo de Apoio a Madeira |

* Tabela **SF2 – Cabeçalho das NF de Saída**

|  |  |
| --- | --- |
| **Campo** | F2\_VALFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFET","MT100",M->F2\_VALFET) |
| **Cabeçalho** | Vl.FETHAB |
| **Descrição** | Valor do FETHAB |
| ***Help*** | Valor calculado na operação referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | F2\_VALFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFAB","MT100",M->F2\_VALFAB) |
| **Cabeçalho** | Vl.FABOV |
| **Descrição** | Valor do FABOV |
| ***Help*** | Valor calculado na operação referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | F2\_VALFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFAC","MT100",M->F2\_VALFAC) |
| **Cabeçalho** | Vl.FACS |
| **Descrição** | Valor do FACS |
| ***Help*** | Valor calculado na operação referente ao FACS. |

|  |  |
| --- | --- |
| **Campo** | F2\_VALFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("NF\_VALFMD","MT100",M->F2\_VALFMD) |
| **Cabeçalho** | Vl.Famad |
| **Descrição** | Valor do Famad |
| ***Help*** | Valor Famad – Fundo de Apoio a Madeira |

* Tabela **SD2 – Itens das NF’s de Saída**

|  |  |
| --- | --- |
| **Campo** | D2\_BASEFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFET","MT100",M->D2\_BASEFET) |
| **Cabeçalho** | Base FETHAB |
| **Descrição** | Base do FETHAB |
| ***Help*** | Base calculada no item referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | D2\_BASEFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFAB","MT100",M->D2\_BASEFAB) |
| **Cabeçalho** | Base FABOV |
| **Descrição** | Base do FABOV |
| ***Help*** | Base calculada no item referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | D2\_BASEFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFAC","MT100",M->D2\_BASEFAC) |
| **Cabeçalho** | Base FACS |
| **Descrição** | Base do FACS |
| ***Help*** | Base calculada no item referente ao FACS. |

|  |  |
| --- | --- |
| **Campo** | D2\_ALIQFET |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALIQFET","MT100",M->D2\_ALIQFET) |
| **Cabeçalho** | Aliq. FETHAB |
| **Descrição** | Aliq. do FETHAB |
| ***Help*** | Alíquota calculada do item referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | D2\_ALIQFAB |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALIQFAB","MT100",M->D2\_ALIQFAB) |
| **Cabeçalho** | Aliq. FABOV |
| **Descrição** | Aliq. do FABOV |
| ***Help*** | Alíquota calculada do item referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | D2\_ALIQFAC |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALIQFAC","MT100",M->D2\_ALIQFAC) |
| **Cabeçalho** | Aliq. FACS |
| **Descrição** | Aliq. do FACS |
| ***Help*** | Alíquota calculada do item referente ao FACS. |

|  |  |
| --- | --- |
| **Campo** | D2\_VALFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFET","MT100",M->D2\_VALFET) |
| **Cabeçalho** | Vlr. FETHAB |
| **Descrição** | Valor do FETHAB |
| ***Help*** | Valor calculado do item referente ao FETHAB. |

|  |  |
| --- | --- |
| **Campo** | D2\_VALFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFAB","MT100",M->D2\_VALFAB) |
| **Cabeçalho** | Vlr. FABOV |
| **Descrição** | Valor do FABOV |
| ***Help*** | Valor calculado do item referente ao FABOV. |

|  |  |
| --- | --- |
| **Campo** | D2\_VALFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFAC","MT100",M->D2\_VALFAC) |
| **Cabeçalho** | Vlr. FACS |
| **Descrição** | Valor do FACS |
| ***Help*** | Valor calculado do item referente ao FACS. |

|  |  |
| --- | --- |
| **Campo** | D2\_BASEFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFMD","MT100",M->D2\_BASEFMD) |
| **Cabeçalho** | Base Famad |
| **Descrição** | Base do Famad |
| ***Help*** | Base Famad – Fundo de Apoio a Madeira |

|  |  |
| --- | --- |
| **Campo** | D2\_ALQFMD |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALQFMD","MT100",M->D2\_ALQFMD) |
| **Cabeçalho** | Aliq. Famad |
| **Descrição** | Alíquota do Famad |
| ***Help*** | Alíquota Famad – Fundo de Apoio a Madeira |

|  |  |
| --- | --- |
| **Campo** | D2\_VALFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFMD","MT100",M->D2\_VALFMD) |
| **Cabeçalho** | Vlr. Famad |
| **Descrição** | Valor do Famad |
| ***Help*** | Valor Famad – Fundo de Apoio a Madeira |

* Tabela **SF3 – Livros Fiscais**

|  |  |
| --- | --- |
| **Campo** | F3\_VALFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Valor FETHAB |
| **Descrição** | Valor do FETHAB |
| ***Help*** | Campo com o valor do FETHAB para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | F3\_VALFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Valor FABOV |
| **Descrição** | Valor do FABOV |
| ***Help*** | Campo com o valor do FABOV para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | F3\_VALFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Valor FACS |
| **Descrição** | Valor do FACS |
| ***Help*** | Campo com o valor do FACS para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | F3\_VALFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("LF\_VALFMD","MT100",M->F3\_VALFMD) |
| **Cabeçalho** | Valor Famad |
| **Descrição** | Valor do Famad |
| ***Help*** | Valor Famad – Fundo de Apoio a Madeira |

* Tabela **SFT – Livros Fiscais por Item de NF**

|  |  |
| --- | --- |
| **Campo** | FT\_BSEFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Base Fethab |
| **Descrição** | Base do FETHAB |
| ***Help*** | Campo com a base do FETHAB para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_BSEFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Base FABOV |
| **Descrição** | Base do FABOV |
| ***Help*** | Campo com a base do FABOV para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_BSEFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Base FACS |
| **Descrição** | Base do FACS |
| ***Help*** | Campo com a base do FACS para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_ALQFET |
| **Tipo** | Numérico |
| **Tamanho** | 6 |
| **Decimal** | 3 |
| **Formato** | @! |
| **Cabeçalho** | Aliq FETHAB |
| **Descrição** | Alíquota do FETHAB |
| ***Help*** | Campo com a alíquota do FETHAB para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_ALQFAB |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @! |
| **Cabeçalho** | Aliq FABOV |
| **Descrição** | Alíquota do FABOV |
| ***Help*** | Campo com a alíquota do FABOV para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_ALQFAC |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @! |
| **Cabeçalho** | Aliq FACS |
| **Descrição** | Alíquota do FACS |
| ***Help*** | Campo com a alíquota do FACS para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_VALFET |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Val FETHAB |
| **Descrição** | Valor do FETHAB |
| ***Help*** | Campo com o valor do FETHAB para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_VALFAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Val FABOV |
| **Descrição** | Valor do FABOV |
| ***Help*** | Campo com o valor do FABOV para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_VALFAC |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Val FACS |
| **Descrição** | Valor do FACS |
| ***Help*** | Campo com o valor do FACS para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Campo** | FT\_BASEFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_BASEFMD","MT100",M->FT\_BASEFMD) |
| **Cabeçalho** | Base Famad |
| **Descrição** | Base do Famad |
| ***Help*** | Base Famad – Fundo de Apoio a Madeira |

|  |  |
| --- | --- |
| **Campo** | FT\_ALQFMD |
| **Tipo** | Numérico |
| **Tamanho** | 5 |
| **Decimal** | 2 |
| **Formato** | @E 99.99 |
| **Validação** | MaFisRef("IT\_ALQFMD","MT100",M->FT\_ALQFMD) |
| **Cabeçalho** | Aliq Famad |
| **Descrição** | Aliquota do Famad |
| ***Help*** | Alíquota Famad – Fundo de Apoio a Madeira |

|  |  |
| --- | --- |
| **Campo** | FT\_VALFMD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Validação** | MaFisRef("IT\_VALFMD","MT100",M->FT\_VALFMD) |
| **Cabeçalho** | Val Famad |
| **Descrição** | Valor do Famad |
| ***Help*** | Valor Famad – Fundo de Apoio a Madeira |

* Tabela **SE1 – Contas a Receber**

|  |  |
| --- | --- |
| **Campo** | E1\_FETHAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr.FETHAB |
| **Descrição** | Valor do tributo FETHAB |
| ***Help*** | Valor do tributo FETHAB. |

|  |  |
| --- | --- |
| **Campo** | E1\_FABOV |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr. FABOV |
| **Descrição** | Valor do tributo FABOV |
| ***Help*** | Valor do tributo FABOV. |

|  |  |
| --- | --- |
| **Campo** | E1\_FACS |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr.FACS |
| **Descrição** | Valor do tributo FACS |
| ***Help*** | Valor do tributo FACS. |

|  |  |
| --- | --- |
| **Campo** | E1\_IMA |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr. IMA |
| **Descrição** | Valor do Imposto IMA |
| ***Help*** | Valor do Imposto IMA. |

|  |  |
| --- | --- |
| **Campo** | E1\_PARCFET |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc.FETHAB |
| **Descrição** | Parcela do tributo FETHAB |
| ***Help*** | Parcela do tributo FETHAB. |

|  |  |
| --- | --- |
| **Campo** | E1\_PARCFAB |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc.FABOV |
| **Descrição** | Parcela do tributo FABOV |
| ***Help*** | Parcela do tributo FABOV. |

|  |  |
| --- | --- |
| **Campo** | E1\_PARCFAC |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc.FACS |
| **Descrição** | Parcela do tributo FACS |
| ***Help*** | Parcela do tributo FACS. |

|  |  |
| --- | --- |
| **Campo** | E1\_PARCIMA |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc. IMA |
| **Descrição** | Parcela do Imposto IMA |
| ***Help*** | Parcela do Impsoto IMA. |

|  |  |
| --- | --- |
| **Campo** | E1\_FAMAD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vl.FAMAD |
| **Descrição** | Valor do Famad |
| **Usado** | Sim |
| **Obrigatório** | Não |
| ***Help*** | Valor do tributo FAMAD. |

|  |  |
| --- | --- |
| **Campo** | E1\_PARCFAM |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Parc.FAMAD |
| **Descrição** | Parcela do tributo Famad |
| **Usado** | Sim |
| **Obrigatório** | Não |
| ***Help*** | Parcela do FAMAD |

* Tabela **SE2 – Contas a Pagar**

|  |  |
| --- | --- |
| **Campo** | E2\_FETHAB |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr.FETHAB |
| **Descrição** | Valor do tributo FETHAB |
| ***Help*** | Valor do tributo FETHAB. |

|  |  |
| --- | --- |
| **Campo** | E2\_FABOV |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr.FABOV |
| **Descrição** | Valor do tributo FABOV |
| ***Help*** | Valor do tributo FABOV. |

|  |  |
| --- | --- |
| **Campo** | E2\_FACS |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr.FACS |
| **Descrição** | Valor do tributo FACS |
| ***Help*** | Valor do tributo FACS. |

|  |  |
| --- | --- |
| **Campo** | E2\_IMA |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr. IMA |
| **Descrição** | Valor do Imposto IMA |
| ***Help*** | Valor do Imposto IMA. |

|  |  |
| --- | --- |
| **Campo** | E2\_PARCFET |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc.FETHAB |
| **Descrição** | Parcela do tributo FETHAB |
| ***Help*** | Parcela do tributo FETHAB. |

|  |  |
| --- | --- |
| **Campo** | E2\_PARCFAB |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc.FABOV |
| **Descrição** | Parcela do tributo FABOV |
| ***Help*** | Parcela do tributo FABOV. |

|  |  |
| --- | --- |
| **Campo** | E2\_PARCFAC |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc.FACS |
| **Descrição** | Parcela do tributo FACS |
| ***Help*** | Parcela do tributo FACS. |

|  |  |
| --- | --- |
| **Campo** | E2\_PARCIMA |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Parc. IMA |
| **Descrição** | Parcela do Imposto IMA |
| ***Help*** | Parcela do Imposto IMA. |

|  |  |
| --- | --- |
| **Campo** | E2\_FAMAD |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Título** | Vl.FAMAD |
| **Descrição** | Valor do Famad |
| **Usado** | Sim |
| **Obrigatório** | Não |
| ***Help*** | Valor do tributo FAMAD. |

|  |  |
| --- | --- |
| **Campo** | E2\_PARCFAM |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Parc.FAMAD |
| **Descrição** | Parcela do tributo Famad |
| **Usado** | Sim |
| **Obrigatório** | Não |
| ***Help*** | Parcela do FAMAD. |

No **Configurador (SIGACFG)**, acesse **Módulo/Cadastros/ Parâmetros**, observe a configuração dos parâmetros a seguir. Caso não existam, é necessário criá-los conforme a seguinte estrutura:

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_FETNAT |
| **Tipo** | Caracter |
| **Conteúdo** | FETHAB |
| **Descrição** | Indica a natureza para o tributo FETHAB para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_FABNAT |
| **Tipo** | Caracter |
| **Conteúdo** | FABOV |
| **Descrição** | Indica a natureza para o tributo FABOV para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_FACNAT |
| **Tipo** | Caracter |
| **Conteúdo** | FACS |
| **Descrição** | Indica a natureza para o tributo FACS para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_IMANAT |
| **Tipo** | Caracter |
| **Conteúdo** | IMA |
| **Descrição** | Indica a natureza para o tributo IMA para o Estado do Mato Grosso. |

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_INDUPF |
| **Tipo** | Caracter |
| **Conteúdo** | M2\_MOEDA5, <A critério do cliente> |
| **Descrição** | Informe o campo que deve ser utilizado da tabela SM2 para informar o indexador  UPF/MT. Ex: M2\_MOEDA5 |

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_AGFETHA |
| **Tipo** | Lógico |
| **Conteúdo** | .T. ou .F. |
| **Descrição** | Controla se irão aglutinar os títulos gerados no Financeiro de FETHAB, FACS e FABOV. |

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_ICMVENC |
| **Tipo** | Caracter |
| **Conteúdo** | Dia correspondente ao vencimento do ICMS |
| **Descrição** | Informar a quantidade de dias uteis para pgto.ICMS e período de apuração, a ser utilizado no cálculo do custo de entrada nas moedas 2, 3, 4 e 5. |

## Procedimento para Configuração

**PRÉ REQUISITO**

Para efetuar o cálculo do FETHAB, FABOV, FAC ,FAMAD ou IMA nos **Documento de Entrada****(****MATA103****)** ou nos **Documento de Saída (MATA460A)** , é necessário:

* O valor da UPF/MT deve constar no campo da moeda, informado no parâmetro **MV\_INDUPF**.
* O conteúdo deste parâmetro **MV\_ICMVENC** é fundamental para determinar a data de vencimento do FETHAB, FABOV e FAC.
* No **Cadastro de Produtos (MATA010)**, informe a alíquota do tributo a ser calculado,.
* Informado na TES que o tributo será calculado.
* No **Cadastro de Clientes (MATA030)** e **Cadastro de Fornecedor (MATA020)**, informe a responsabilidade de recolhimento dos tributos.

Importante

É obrigatório que a primeira ou segunda unidade de medida utilizada seja a unidade de medida informada no cálculo.

Exemplos:

* **FETHAB Soja** – É obrigatório que a primeira ou segunda unidade de medida utilizada seja tonelada.
* **FETHAB Algodão** – É obrigatório que a primeira ou segunda unidade de medida utilizada seja tonelada.
* **FETHAB Gado** – É obrigatório que a primeira ou segunda unidade de medida utilizada seja unidade.
* **FETHAB Madeira**- É obrigatório que a primeira ou segunda unidade de medida utilizada seja Metros Cúbicos.
* **FACS Soja** – É obrigatório que a primeira ou segunda unidade de medida utilizada seja tonelada.
* **FABOV Gado** – É obrigatório que a primeira ou segunda unidade de medida utilizada seja unidade.
* **FAMAD Madeira**- É obrigatório que a primeira ou segunda unidade de medida utilizada seja Metros Cúbicos
* **IMA Algodão** - É obrigatório que a primeira ou segunda unidade de medida utilizada seja tonelada.

Ao iniciar os procedimentos, é fundamental que a moeda utilizada para informar a UPF no Sistema seja aquela informada no parâmetro **MV\_INDUPF**.

**PROCEDIMENTOS**

1. Em **Livros Fiscais (SIGAFIS)**, acesse **Atualizações/Cadastro/Cadastro de Produtos (MATA010)**, configure as alíquotas dos impostos e preencha os campos **Aliq. FACS**, **Tipo FETHAB**, **Aliq. FETHAB**, **Aliq. FABOV, Aliq. FAMAD ou Aliq.IMA.**
2. Acesse o **Cadastro de Clientes (MATA030)** e configure a responsabilidade de recolhimento no campo **Rec. FETHAB, Rec. FABOV, Rec. FAMAD**ou**Rec. IMA-MT**.
3. Acesse o **Cadastro de TES (MATA080)**e na pasta **Impostos**, ajuste o campo **Calc. FETHAB, Calc. FACS, Calc. FABOV, Calc. Famad**ou**Calc. IMA-MT** com a opção **Sim**.
4. Em **Faturamento (SIGAFAT)** , acesse**Atualizações/Pedido de Venda (MATA410)**, selecione **Incluir** para inserir um pedido de venda. Preencha os campos desejados.
5. Clique na opção **Planilha Financeira**no *menu* desta rotina e veja, na pasta**Nota Fiscal**, as informações serão demonstrados nas colunas**Base Imposto**,**Alíquota**e**Vlr. Imposto.**
6. Realize a conferência e clique em**Sair.**
7. Fature o pedido de venda por meio da rotina **Atualizações/Faturamento/Documento de Saída (MATA460A)**.
8. Clique na opção **Visualizar**.
9. Acesse a pasta **Impostos** e verifique  as informações referentes a  em **Base Imposto**,**Alíquota**e**Vlr. Imposto.**
10. Em **Financeiro (SIGAFIN)**, acesse **Atualizações/Contar a Receber/Contas a Receber (FINA040)**, clique em **Visualizar** para conferir os títulos gerados. Veja o título a receber no valor total na Nota Fiscal, por meio do campo **Vlr. Título**. Verifique também o titulo do tributo IMA, através do campo E1\_TIPO = "IM-".
11. Em **Financeiro (SIGAFIN)**, acesse **Atualizações/Contar a Pagar/Contas a Pagar (FINA050)**, clique em **Visualizar** para conferir ostítulos a pagar do tributo calculado. Os campos relacionados são: **Natureza**, **Vlr. Título** e **Tipo**. Verifique também o titulo do tributo IMA, através do campo E2\_TIPO = "IMA".

## Informações Técnicas

|  |  |
| --- | --- |
| **A quem se destina** | Aos contribuintes que promoverem saídas de produtos agrícolas e da pecuária e a exploração dos recursos minerais indicados nas condições que especifica, bem como para os substitutos tributários nas operações com combustíveis e dá outras providências. |
| **Prazo de Entrega** | Não há. A contribuição será calculada nos lançamentos das notas fiscais de compra e venda.  Entradas,  a data de vencimento dos títulos é configurada através do parâmetro MV\_ICMVENC.  Caso o parâmetro esteja preenchido o sistema obedecerá a seguinte regra;  - Se a data for igual a 6 , caindo em dia não útil o vencimento real do título da contribuição deverá ser prorrogado para o próximo dia útil.  - Se a data for diferente de 6, o vencimento deve ser antecipado para o dia útil anterior.  Caso o parâmetro esteja em branco será adota o mesmo procedimento atual, considerando a data de emissão da nota fiscal.  Saídas, a data de vencimento dos títulos é a data da emissão da nota fiscal. |
| **Competência** | Estadual – MT |
| **Onde encontrar o Decreto** | [http://www.sefaz.mt.gov.br](http://www.sefaz.mt.gov.br/) |
| **Legislação contemplada** | Lei nº 7.263, de 27 de março de 2000 |

|  |  |
| --- | --- |
| **Campo** | E2\_FACS |
| **Tipo** | Numérico |
| **Tamanho** | 14 |
| **Decimal** | 2 |
| **Formato** | @E 99,999,999,999.99 |
| **Cabeçalho** | Vlr.FACS |
| **Descrição** | Valor do tributo FACS |
| ***Help*** | Valor do tributo FACS. |

|  |  |
| --- | --- |
| **Tabelas Utilizadas** | SB1 – Cadastro de Produtos  SA1 – Cadastro de Clientes  SA2 – Cadastro de Fornecedores  SF4 – Tipo de entrada e saída  SF1 – Cabeçalho da nota fiscal de entrada  SD1 – Itens da nota fiscal de entrada  SF2 – Cabeçalho da nota fiscal de saída  SD2 – Itens da nota fiscal de saída  SF3 – Livros fiscais  SFT – Livro fiscal por item de nota  SE1 – Títulos a receber  SE2 – Títulos a pagar |
| **Rotinas Envolvidas** | MATA410 - Pedidos de Venda  FINA050 - Contas a Pagar  FINA040 - Contas a Receber  MATA460A – Documento de Saída  MATA080 - Tipos de Ent/Saida  MATA030 - Clientes  MATA020 - Fornecedor  MATA010 – Produtos  MATA103 – Documento de Entrada |
| **Sistemas Operacionais** | Windows®/Linux® |

*Link contendo as informações acima:*

*<http://tdn.totvs.com/display/public/PROT/FIS0004_FETHAB_FACS_FABOV_FAMAD_IMA_FASE_MT>*

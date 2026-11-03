---
content_hash: 6f5d84abc745bfe92bf571830c45c82301ef549e62c5850fd62d612f73034665
fetched_at: '2026-06-29T00:08:29.632127+00:00'
page_id: '272153983'
product: rm
source: tdn-rm
title: Exportação e Importação de Dados do Funcionário (XLB)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272153983
version: 105
---

```

```

Este processo foi desenvolvido para auxiliar as equipes de suporte e desenvolvimento da TOTVS na simulação e resolução de problemas reportados pelos clientes, especialmente quando tais situações não puderam ser reproduzidas em nossas bases de teste.

1true1Exportação do XLBPasso a Passo Exportação

## **Exportação dos Dados do Funcionário**

Para gerar o arquivo de restauração de dados em formato XML, siga os seguintes passos:

* Na barra lateral do produto, localize o item **“Executar”**;
* Selecione a action **“FopRestauracaoAction”** conforme ilustrado na imagem abaixo:

Após executar a **Action**, será exibido um **assistente (Wizard)** que irá conduzir a execução do processo.

No assistente, será necessário:

* Marcar a opção **“Exportar”**
* Informar a **chapa do funcionário**
* Incluir os **processos relacionados à demanda**

Essas informações são essenciais para que o sistema possa **gerar o XML** e permitir a simulação precisa do problema.

2Tabelas e Menus ExportadosTabelas e Menus Exportados

## **Tabelas e Campos que serão exportados/importados:**

| ITEM | TABELA | MENU | RELEASE |
| --- | --- | --- | --- |
| 1 | GSISTEMA | Pega contexto |  |
| 2 | PADICRESC | RH | Folha de Pagamento | Configurações | Parametrizador |  |
| 3 | PGADIC13 | RH | Folha de Pagamento | Configurações | Parametrizador |  |
| 4 | PPARAM | RH | Folha de Pagamento | Configurações | Parametrizador |  |
| 5 | PPARAMADICIONAIS | RH | Folha de Pagamento | Configurações | Parametrizador |  |
| 6 | PPARAMRELAT | RH | Folha de Pagamento | Configurações | Parametrizador |  |
| 7 | PBASESAL | RH | Folha de Pagamento | Configurações | Parametrizador |  |
| 8 | PLANCFINANC | RH | Folha de Pagamento | Encargos | Cadastros Financeiros | Parametrização de Lançamentos Financeiros |  |
| 9 | PFMOVTOMADOR | RH | Folha de Pagamento | Encargos | FGTS | Editar distribuição Tomador |  |
| 10 | PFENCARGO | RH | Folha de Pagamento | Encargos | Históricos | Encargos |  |
| 11 | PDADOSDIS | RH | Folha de Pagamento | eSocial | Acordo Coletivo / Reajuste por Lei |  |
| 12 | PLOGFUNCIONARIO | RH | Folha de Pagamento | Folha Mensal | Consulta | Gerenciador de Log de Cálculo |  |
| 13 | GAGENCIA | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Bancos/Agências |  |
| 14 | GCALEND | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Calendários |  |
| 15 | GFERIADO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Calendários |  Feriados |  |
| 16 | GCOLIGADA | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Coligadas |  |
| 17 | GFILIAL | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Filiais |  |
| 18 | GMOEDA | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Moedas e Índices |  |
| 19 | PRUBRICA | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | HOMOLOGRUB |  |
| 20 | PCODINTCONTFUNC | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INTCONTFUN |  |
| 21 | PCODINTGERFUNC | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INTGERFUNC |  |
| 22 | PCODCALCULO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT19 |  |
| 23 | PMOTADMISSAO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT22 |  |
| 24 | PMOTDEMISSAO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT23 |  |
| 25 | PMOTMUDSECAO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT24 |  |
| 26 | PMOTMUDFUNCAO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT25 |  |
| 27 | PMOTMUDSAL | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT26 |  |
| 28 | PMUDSITUACAO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT28 |  |
| 29 | PCODEMPRT | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT30 |  |
| 30 | PCODVALSIND | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT32 |  |
| 31 | PCODTOTALIZ | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT33 |  |
| 32 | PTPPENSAO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT45 |  |
| 33 | PTPTABCALC | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Tabela Dinâmicas | INT50 |  |
| 34 | PCALCVLR | RH | Folha de Pagamento | Administração Pessoal | Cálculos | Tabelas de Cálculo |  |
| 35 | PTABCALC | RH | Folha de Pagamento | Administração Pessoal | Cálculos | Tabelas de Cálculo |  |
| 36 | PVALFIX | RH | Folha de Pagamento | Administração Pessoal | Cálculos | Valores Fixos |  |
| 37 | PCARGO | RH | Folha de Pagamento | Administração Pessoal | Cargos/Funções | Cargos |  |
| 38 | PFUNCAO | RH | Folha de Pagamento | Administração Pessoal | Cargos/Funções | Funções |  |
| 39 | PCCUSTO | RH | Folha de Pagamento | Administração Pessoal | Centros Custos |  |
| 40 | FCFO | RH | Folha de Pagamento | Administração Pessoal | Cliente e Fornecedor |  |
| 41 | FIRRF | RH | Folha de Pagamento | Administração Pessoal | Cliente e Fornecedor | Tributos | Natureza de Rendimento |  |
| 42 | PEVENTO | RH | Folha de Pagamento | Administração Pessoal | Eventos | Eventos |  |
| 43 | PRATEIO | RH | Folha de Pagamento | Administração Pessoal | Eventos | Rateio de Eventos |  |
| 44 | GFORMULA | RH | Folha de Pagamento | Administração Pessoal | Formulas |  |
| 45 | AHORARIO | RH | Folha de Pagamento | Administração Pessoal | Horários |  |
| 46 | ABATHOR | RH | Folha de Pagamento | Administração Pessoal | Horários | Anexos | Jornada |  |
| 47 | AINDHOR | RH | Folha de Pagamento | Administração Pessoal | Horários | Anexos | Jornada |  |
| 48 | GDEPTO | RH | Folha de Pagamento | Administração Pessoal | Seção |  |
| 49 | PSECAO | RH | Folha de Pagamento | Administração Pessoal | Seção |  |
| 50 | PFUNC | RH | Folha de Pagamento | Administração Pessoal | Funcionários |  |
| 51 | GBANCO | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Banco Pgto / Financeiro | Banco de Pagamento |  |
| 52 | FCONTA | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Banco Pgto / Financeiro |  |
| 53 | GCCUSTO | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Dados Contábeis |  |
| 54 | PFUFERIAS | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Férias |  |
| 55 | PFUFERIASPER | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Férias |  |
| 56 | PFUFERIASRECIBO | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Férias | Visualizar Recibo |  |
| 57 | PFUFERIASVERBAS | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Férias | Visualizar Recibo |  |
| 58 | PGADICFER | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Férias | Anexos | Adicionais de férias |  |
| 59 | PDADOSRESCISAO | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Rescisão |  |
| 60 | PFFINANC | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Movimento | Ficha financeira |  |
| 61 | PFPERFF | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Movimento | Ficha financeira |  |
| 62 | PFVERBASDIS | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Movimento | Ficha financeira |  |
| 63 | PFDEPEND | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Dependentes |  |
| 64 | PFDEPMOV | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Dependentes | Anexos | Movimento da Pensão de Dependentes |  |
| 65 | PFRATEIOFIXO | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Rateio Fixo |  |
| 66 | PFSALCMP | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Salário Composto |  |
| 67 | PFSALCMPCC | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Salário Composto |  |
| 68 | PFENCCC | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Centro de Custo |  |
| 69 | PFHSTFCO | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Históricos | Histórico de Função |  |
| 70 | PFHSTSEC | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Históricos | Histórico de Seção |  |
| 71 | PFHSTRATEIOTOMADOR | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Históricos | Histórico de Rateio por Tomador |  |
| 72 | PFHSTSAL | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Históricos | Histórico Salarial |  |
| 73 | PFHSTASSMED | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Históricos | Histórico Assistência Saúde |  |
| 74 | VFAIXASALARIAL | RH | Gestão de Pessoas | Valorização | Faixas Salariais |  |
| 75 | VNIVELFUNCAO | RH | Gestão de Pessoas | Valorização | Níveis Salariais |  |
| 76 | VTABSALARIAIS | RH | Gestão de Pessoas | Valorização | Tabelas Salariais |  |
| 77 | PPESSOA | RH | Gestão de Pessoas | Acompanhamento | Pessoas |  |
| 78 | GCONSSQL | RH | Folha de Pagamento | Configurações | Visões SQL | 12.1.2410.296, 12.1.2502.200, 12.1.2506.142 e superiores. |
| 79 | GCOTACAO | RH | Folha de Pagamento | Administração Pessoal | Cadastros Globais | Cotações | 12.1.2410.300, 12.1.2502.209, 12.1.2506.155 e superiores. |
| 80 | VPCOMPL | RH | Gestão de Pessoas | Acompanhamento | Pessoas | Campos Complementares | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 81 | PFCOMPL | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Campos Complementares | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 82 | PFMOVFGTS | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Manutenção do FGTS | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 83 | PFEMPRT | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Empréstimos | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 84 | PEQUIPE | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Identificação | Código da Equipe | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 85 | PEVTMED | RH | Folha de Pagamento | Administração Pessoal | Eventos | Eventos | Anexos | Eventos de Média | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 86 | PSINDEVT | RH | Folha de Pagamento | Administração Pessoal | Sindicatos | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 87 | PSINDIC | RH | Folha de Pagamento | Administração Pessoal | Sindicatos | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 88 | PSINDMED | RH | Folha de Pagamento | Administração Pessoal | Sindicatos | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 89 | PSINDREMBASE | RH | Folha de Pagamento | Administração Pessoal | Sindicatos | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 90 | PSINDVAL | RH | Folha de Pagamento | Administração Pessoal | Sindicatos | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 91 | GACESSO | Serviços Globais | Segurança | Códigos de Acesso | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 92 | GPERFIL | Serviços Globais | Segurança | Perfis | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 93 | GUSRPERFIL | Serviços Globais | Segurança | Perfis | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 94 | GPERMIS | Serviços Globais | Segurança | Perfis | Acesso a menus | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 95 | GAUTZMENU | Serviços Globais | Segurança | Perfis | Acesso a menus | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 96 | GUSUARIO | Serviços Globais | Segurança | Usuários | 12.1.2410.290, 12.1.2502.193, 12.1.2506.134 e superiores. |
| 97 | GDINAN | RH | Folha de Pagamento | Administração Pessoal | Cadastro Globais  | Tabelas Dinâmicas   Observação: será exportado somente as tabelas de utilização do sistema folha de pagamento | 12.1.2410.294, 12.1.2502.198, 12.1.2506.140 e superiores. |
| 98 | PFCODFIX | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Códigos Fixos | 12.1.2410.298, 12.1.2502.205, 12.1.2506.148 e superiores. |
| 99 | PFDADOSRESIDEXTERIOR | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Folha de Pagamento | Dados do Residente ou Domiciliado no Exterior | 12.1.2502.215,  12.1.2506.164, 12.1.2510.100 e superiores. |
| 100 | STURMADISC | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 101 | SPLETIVO | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 102 | GINTEGRACAO | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 103 | SFILIAL | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 104 | STIPOCURSO | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 105 | SPROFESSOR | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 106 | STITULACAO | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 107 | STURMA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 108 | SPROFESSORTURMA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 109 | VNIVEISTABSALARIAIS | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 110 | VTABELASALARIAL | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 111 | ETURMISTA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 112 | SATIVIDADEPROFESSOR | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 113 | SATIVIDADEEXTRA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 114 | SGRUPOATIVIDADE | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 115 | STURMADISCGERENCIADA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 116 | SHORAAULA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 117 | SHABILITACAOFILIAL | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 118 | SPROFESSORFILIAL | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 119 | SATIVIDADE | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 120 | SHABILITACAOFILIALPROFESSOR | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 121 | SCONTRATO | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 122 | SMATRICULA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 123 | SHABILITACAOFILIALINTPROTHEUS | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 124 | SSTATUS | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 125 | SMATRICPL | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 126 | SDISCIPLINA | Administração de Pessoal | Folha Educacional| Reprogramação Salarial | 12.1.2502.229, 12.1.2506.179, 12.1.2510.112 e superiores. |
| 127 | PVALETR | RH | Administração e Pessoal | Vale Transporte | 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e superiores |
| 128 | PTARIFA | RH | Administração e Pessoal | Vale Transporte | Código Tarifa | 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e superiores |
| 129 | PCODITINER | RH | Administração e Pessoal | Vale Transporte | Código Itinerário | 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e superiores |
| 130 | PGRPVALE | RH | Administração e Pessoal | Vale Transporte | Grupo Transporte | 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e superiores |
| 131 | PMEIOTRANSP | RH | Administração e Pessoal | Vale Transporte | Tipo Transporte | 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e superiores |
| 132 | PFVALETR | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Parâmetros | 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e superiores |
| 133 | PFHSTCODTIPOFUNCIONARIO | RH | Folha de Pagamento | Administração Pessoal | Funcionários | Anexos | Históricos | Histórico Tipo Funcionário | 12.1.2502.237, 12.1.2506.186, 12.1.2510.119 e superiores |
| 134 | PFREEMBOLSOOPERADORA | RH | Folha de Pagamento | eSocial | Operadora Saúde | 12.1.2502.256, 12.1.2506.214, 12.1.2510.142 e superiores |
| 135 | VENTIDADES | RH | Gestão de Pessoas | Desenvolvimento| Entidades | 12.1.2502.256, 12.1.2506.214, 12.1.2510.142 e superiores |

3Importação do XLB (EXCLUSIVO TOTVS)Importação do XLB (EXCLUSIVO TOTVS)

## **Importação dos Dados do Funcionário (EXCLUSIVO PARA UTILIZAÇÃO DO SUPORTE DA TOTVS - NÃO DEVE SER UTILIZADO PELO CLIENTE)**

**Pré-requisitos:**

* Backup da base de dados completo.
* Acesso ao servidor com o **RM.exe.config**.
* Acesso ao Host Branco.

### **Etapas:**

**1. Restaurar backup da base vazia:**

* Siga as instruções específicas da ferramenta de backup utilizada para restaurar a base em um estado vazio.
* Link de base vazia na versão 12.1.2406: <https://drive.google.com/file/d/1bue680TrIJCX6oj4yGaIFmjkItW3rI8X/view?usp=drive_link>
  + se for utilizar essa base, você pode alterar o alias e pular para a etapa 5.

**2. Executar o script para criar os usuários no banco:**

* Execute o script para atualizar as informações do usuário na base de dados.

**3. Alterar o alias:**

* Modifique o alias para apontar para a nova base de dados. Consulte a documentação do seu sistema para obter instruções específicas.

**4. Executar o Atualizador:**

* Execute o Atualizador para aplicar as atualizações necessárias à nova base de dados.

**5. Executar o TOTVS Audit:**

* Execute o Totvs Audit para verificar a integridade da base de dados após a restauração.

**6. Habilitar restauração de base no HOST:**

* No arquivo **`RM.exe.config`**, localize a seção `<appSettings>` e adicione a seguinte chave: <add key="EnableBaseRestore" value="true" />

**7. Iniciar o HOST e logar no Host Branco:**

* Inicie o serviço HOST.
* Acesse o Host Branco utilizando seu usuário e senha.

**8. Rode na base seguinte SQL para desabilitar verificação de chaves estrangeiras:**

ALTER TABLE PSECAO NOCHECK CONSTRAINT FKPSECAO\_GCALEND

ALTER TABLE PEVENTO NOCHECK CONSTRAINT FKPEVENTO\_CHISTP

ALTER TABLE PEVENTO NOCHECK CONSTRAINT FKPEVENTO\_PGRPCONTACONTCC

ALTER TABLE PEVENTO NOCHECK CONSTRAINT FKPEVENTO\_PGRPCONTACONTCD

ALTER TABLE PLANCFINANC NOCHECK CONSTRAINT FKLANCFINANC\_FTDO

ALTER TABLE PLANCFINANC NOCHECK CONSTRAINT FKPLANCFINANC\_FCXA

ALTER TABLE PFHSTAFT NOCHECK CONSTRAINT FKPFHSTAFT\_VPROFISSIONALSAUDE

ALTER TABLE PCCUSTO NOCHECK CONSTRAINT FKPCCUSTO\_PCODINTCONT

ALTER TABLE PCCUSTO NOCHECK CONSTRAINT FKPCCUSTO\_GCCUSTO

ALTER TABLE PCCUSTO NOCHECK CONSTRAINT FKPCCUSTO\_PCODINTGER

ALTER TABLE PSECAO NOCHECK CONSTRAINT FKPSECAO\_PCCUSTO

ALTER TABLE PSECAO NOCHECK CONSTRAINT FKPSECAO\_PCODINTCONT

ALTER TABLE PFUNC NOCHECK CONSTRAINT FKPFUNC\_FCFO

ALTER TABLE PFMOVTOMADOR NOCHECK CONSTRAINT FKPFMOVTOMADOR\_FCFO

ALTER TABLE FCFO NOCHECK CONSTRAINT FKFCFO\_DNATUREZARENDIMENTO

ALTER TABLE PEVENTO NOCHECK CONSTRAINT FKPEVENTO\_PGRPCONTAGERCD

ALTER TABLE PEVENTO NOCHECK CONSTRAINT FKPEVENTO\_PGRPCONTAGERCC

ALTER TABLE PFHSTRATEIOTOMADOR NOCHECK CONSTRAINT FKPFHSTRATEIOTOMADOR\_FCFO

ALTER TABLE FCXA NOCHECK CONSTRAINT FKFCXA\_FCONTA

ALTER TABLE PLANCFINANC NOCHECK CONSTRAINT FKPLANCFINANC\_FCFO

ALTER TABLE GAGENCIA NOCHECK CONSTRAINT FKGAGENCIA\_GETD

ALTER TABLE FCXA NOCHECK CONSTRAINT FKFCXA\_FLIQUIDEZ

ALTER TABLE PSECAO NOCHECK CONSTRAINT FKPSECAO\_PCODINTGER

ALTER TABLE PFMOVFGTS NOCHECK CONSTRAINT FKPFMOVFGTS\_PFUNC

ALTER TABLE GUSUARIO NOCHECK CONSTRAINT  FKGUSUARIO\_GACESSO

ALTER TABLE PENCARGO NOCHECK CONSTRAINT  FKPENCARGO\_CHISTP

ALTER TABLE PENCARGO NOCHECK CONSTRAINT FKPENCARGO\_PGRPCONTACONTCC

ALTER TABLE PENCARGO NOCHECK CONSTRAINT FKPENCARGO\_PGRPCONTACONTCD

ALTER TABLE GPERMIS NOCHECK CONSTRAINT FKGPERMIS\_GCOLIGADA

ALTER TABLE PSERVBANCO NOCHECK CONSTRAINT FKPSERVBANCO\_GDINAM

ALTER TABLE PGRPVALE NOCHECK CONSTRAINT FKPGRPVALE\_GCOLIGADA

ALTER TABLE PCODITINER NOCHECK CONSTRAINT FKPCODITINER\_GCOLIGADA

ALTER TABLE PMSGCRITICA NOCHECK CONSTRAINT FKPMSGCRITICA\_GCOLIGADA

ALTER TABLE PCODACUM NOCHECK CONSTRAINT FKPCODACUM\_GCOLIGADA

ALTER TABLE PCODGRPAAS NOCHECK CONSTRAINT FKPCODGRPAAS\_GCOLIGADA

ALTER TABLE PCODVALSEC NOCHECK CONSTRAINT FKPCODVALSEC\_GCOLIGADA

ALTER TABLE PCODINCDEP NOCHECK CONSTRAINT FKPCODINCDEP\_GCOLIGADA

ALTER TABLE STURMADISC NOCHECK CONSTRAINT ALL;

ALTER TABLE SPLETIVO NOCHECK CONSTRAINT ALL;

ALTER TABLE GINTEGRACAO NOCHECK CONSTRAINT ALL;

ALTER TABLE SFILIAL NOCHECK CONSTRAINT ALL;

ALTER TABLE STIPOCURSO NOCHECK CONSTRAINT ALL;

ALTER TABLE SPROFESSOR NOCHECK CONSTRAINT ALL;

ALTER TABLE STITULACAO NOCHECK CONSTRAINT ALL;

ALTER TABLE STURMA NOCHECK CONSTRAINT ALL;

ALTER TABLE SPROFESSORTURMA NOCHECK CONSTRAINT ALL;

ALTER TABLE VNIVEISTABSALARIAIS NOCHECK CONSTRAINT ALL;

ALTER TABLE VTABELASALARIAL NOCHECK CONSTRAINT ALL;

ALTER TABLE ETURMISTA NOCHECK CONSTRAINT ALL;

ALTER TABLE SATIVIDADEPROFESSOR NOCHECK CONSTRAINT ALL;

ALTER TABLE SATIVIDADEEXTRA NOCHECK CONSTRAINT ALL;

ALTER TABLE SGRUPOATIVIDADE NOCHECK CONSTRAINT ALL;

ALTER TABLE STURMADISCGERENCIADA NOCHECK CONSTRAINT ALL;

ALTER TABLE SHORAAULA NOCHECK CONSTRAINT ALL;

ALTER TABLE SHABILITACAOFILIAL NOCHECK CONSTRAINT ALL;

ALTER TABLE SPROFESSORFILIAL NOCHECK CONSTRAINT ALL;

ALTER TABLE SATIVIDADE NOCHECK CONSTRAINT ALL;

ALTER TABLE SHABILITACAOFILIALPROFESSOR NOCHECK CONSTRAINT ALL;

ALTER TABLE SCONTRATO NOCHECK CONSTRAINT ALL;

ALTER TABLE SMATRICULA NOCHECK CONSTRAINT ALL;

ALTER TABLE SHABILITACAOFILIALINTPROTHEUS NOCHECK CONSTRAINT ALL;

ALTER TABLE SSTATUS NOCHECK CONSTRAINT ALL;

ALTER TABLE SMATRICPL NOCHECK CONSTRAINT ALL;

ALTER TABLE SDISCIPLINA NOCHECK CONSTRAINT ALL;

ALTER TABLE PFSALCMP NOCHECK CONSTRAINT ALL;

          ALTER TABLE STURMADISC NOCHECK CONSTRAINT ALL;

          ALTER TABLE SPLETIVO NOCHECK CONSTRAINT ALL;

          ALTER TABLE GINTEGRACAO NOCHECK CONSTRAINT ALL;

          ALTER TABLE SFILIAL NOCHECK CONSTRAINT ALL;

          ALTER TABLE STIPOCURSO NOCHECK CONSTRAINT ALL;

          ALTER TABLE SPROFESSOR NOCHECK CONSTRAINT ALL;

          ALTER TABLE STITULACAO NOCHECK CONSTRAINT ALL;

          ALTER TABLE STURMA NOCHECK CONSTRAINT ALL;

          ALTER TABLE SPROFESSORTURMA NOCHECK CONSTRAINT ALL;

          ALTER TABLE VNIVEISTABSALARIAIS NOCHECK CONSTRAINT ALL;

          ALTER TABLE VTABELASALARIAL NOCHECK CONSTRAINT ALL;

          ALTER TABLE ETURMISTA NOCHECK CONSTRAINT ALL;

          ALTER TABLE SATIVIDADEPROFESSOR NOCHECK CONSTRAINT ALL;

          ALTER TABLE SATIVIDADEEXTRA NOCHECK CONSTRAINT ALL;

          ALTER TABLE SGRUPOATIVIDADE NOCHECK CONSTRAINT ALL;

          ALTER TABLE STURMADISCGERENCIADA NOCHECK CONSTRAINT ALL;

          ALTER TABLE SHORAAULA NOCHECK CONSTRAINT ALL;

          ALTER TABLE SHABILITACAOFILIAL NOCHECK CONSTRAINT ALL;

          ALTER TABLE SPROFESSORFILIAL NOCHECK CONSTRAINT ALL;

          ALTER TABLE SATIVIDADE NOCHECK CONSTRAINT ALL;

          ALTER TABLE SHABILITACAOFILIALPROFESSOR NOCHECK CONSTRAINT ALL;

          ALTER TABLE SCONTRATO NOCHECK CONSTRAINT ALL;

          ALTER TABLE SMATRICULA NOCHECK CONSTRAINT ALL;

          ALTER TABLE SHABILITACAOFILIALINTPROTHEUS NOCHECK CONSTRAINT ALL;

          ALTER TABLE SSTATUS NOCHECK CONSTRAINT ALL;

          ALTER TABLE SMATRICPL NOCHECK CONSTRAINT ALL;

          ALTER TABLE SDISCIPLINA NOCHECK CONSTRAINT ALL;

          ALTER TABLE PFSALCMP NOCHECK CONSTRAINT ALL;

         ALTER TABLE PVALETR NOCHECK CONSTRAINT FKPVALETR\_PCODITINER

        ALTER TABLE PVALETR NOCHECK CONSTRAINT FKPVALETR\_PGRPVALE

        ALTER TABLE PVALETR NOCHECK CONSTRAINT ALL

      ALTER TABLE VENTIDADES CHECK CONSTRAINT FKVENTIDADES\_VAREASATUACAO;

     ALTER TABLE PFREEMBOLSOOPERADORAMENSAL CHECK CONSTRAINT FKPFREEMBOLSOOPERMENSAL\_PFUNC;

**9. Importar o XLB****:**

* Clique em importar

**10. Rode o script pra voltar as chaves****:**

ALTER TABLE PSECAO CHECK CONSTRAINT FKPSECAO\_GCALEND

ALTER TABLE PEVENTO CHECK CONSTRAINT FKPEVENTO\_CHISTP

ALTER TABLE PEVENTO CHECK CONSTRAINT FKPEVENTO\_PGRPCONTACONTCC

ALTER TABLE PEVENTO CHECK CONSTRAINT FKPEVENTO\_PGRPCONTACONTCD

ALTER TABLE PLANCFINANC CHECK CONSTRAINT FKLANCFINANC\_FTDO

ALTER TABLE PLANCFINANC CHECK CONSTRAINT FKPLANCFINANC\_FCXA

ALTER TABLE PFHSTAFT CHECK CONSTRAINT FKPFHSTAFT\_VPROFISSIONALSAUDE

ALTER TABLE PCCUSTO CHECK CONSTRAINT FKPCCUSTO\_PCODINTCONT

ALTER TABLE PCCUSTO CHECK CONSTRAINT FKPCCUSTO\_GCCUSTO

ALTER TABLE PCCUSTO CHECK CONSTRAINT FKPCCUSTO\_PCODINTGER

ALTER TABLE PSECAO CHECK CONSTRAINT FKPSECAO\_PCCUSTO

ALTER TABLE PSECAO CHECK CONSTRAINT FKPSECAO\_PCODINTCONT

ALTER TABLE PFUNC CHECK CONSTRAINT FKPFUNC\_FCFO

ALTER TABLE PFMOVTOMADOR CHECK CONSTRAINT FKPFMOVTOMADOR\_FCFO

ALTER TABLE FCFO CHECK CONSTRAINT FKFCFO\_DNATUREZARENDIMENTO

ALTER TABLE PEVENTO CHECK CONSTRAINT FKPEVENTO\_PGRPCONTAGERCD

ALTER TABLE PEVENTO CHECK CONSTRAINT FKPEVENTO\_PGRPCONTAGERCC

ALTER TABLE PFHSTRATEIOTOMADOR CHECK CONSTRAINT FKPFHSTRATEIOTOMADOR\_FCFO

ALTER TABLE FCXA CHECK CONSTRAINT FKFCXA\_FCONTA

ALTER TABLE PLANCFINANC CHECK CONSTRAINT FKPLANCFINANC\_FCFO

ALTER TABLE GAGENCIA CHECK CONSTRAINT FKGAGENCIA\_GETD

ALTER TABLE FCXA CHECK CONSTRAINT FKFCXA\_FLIQUIDEZ

ALTER TABLE PSECAO CHECK CONSTRAINT FKPSECAO\_PCODINTGER

ALTER TABLE PFMOVFGTS CHECK CONSTRAINT FKPFMOVFGTS\_PFUNC

ALTER TABLE GUSUARIO CHECK CONSTRAINT  FKGUSUARIO\_GACESSO

ALTER TABLE PENCARGO CHECK CONSTRAINT  FKPENCARGO\_CHISTP

ALTER TABLE PENCARGO CHECK CONSTRAINT FKPENCARGO\_PGRPCONTACONTCC

ALTER TABLE PENCARGO CHECK CONSTRAINT FKPENCARGO\_PGRPCONTACONTCD

ALTER TABLE GPERMIS CHECK CONSTRAINT FKGPERMIS\_GCOLIGADA

ALTER TABLE PSERVBANCO CHECK CONSTRAINT FKPSERVBANCO\_GDINAM

ALTER TABLE PGRPVALE CHECK CONSTRAINT FKPGRPVALE\_GCOLIGADA

ALTER TABLE PCODITINER CHECK CONSTRAINT FKPCODITINER\_GCOLIGADA

ALTER TABLE PMSGCRITICA CHECK CONSTRAINT FKPMSGCRITICA\_GCOLIGADA

ALTER TABLE PCODACUM CHECK CONSTRAINT FKPCODACUM\_GCOLIGADA

ALTER TABLE PCODGRPAAS CHECK CONSTRAINT FKPCODGRPAAS\_GCOLIGADA

ALTER TABLE PCODVALSEC CHECK CONSTRAINT FKPCODVALSEC\_GCOLIGADA

ALTER TABLE PCODINCDEP CHECK CONSTRAINT FKPCODINCDEP\_GCOLIGADA

ALTER TABLE PVALETR CHECK CONSTRAINT FKPVALETR\_PCODITINER;

ALTER TABLE PVALETR CHECK CONSTRAINT FKPVALETR\_PGRPVALE;

ALTER TABLE VENTIDADES CHECK CONSTRAINT FKVENTIDADES\_VAREASATUACAO;

ALTER TABLE PFREEMBOLSOOPERADORAMENSAL CHECK CONSTRAINT FKPFREEMBOLSOOPERMENSAL\_PFUNC;

ALTER TABLE STURMADISC WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SPLETIVO WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE GINTEGRACAO WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SFILIAL WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE STIPOCURSO WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SPROFESSOR WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE STITULACAO WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE STURMA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SPROFESSORTURMA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE VNIVEISTABSALARIAIS WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE VTABELASALARIAL WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE ETURMISTA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SATIVIDADEPROFESSOR WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SATIVIDADEEXTRA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SGRUPOATIVIDADE WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE STURMADISCGERENCIADA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SHORAAULA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SHABILITACAOFILIAL WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SPROFESSORFILIAL WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SATIVIDADE WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SHABILITACAOFILIALPROFESSOR WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SCONTRATO WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SMATRICULA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SHABILITACAOFILIALINTPROTHEUS WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SSTATUS WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SMATRICPL WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE SDISCIPLINA WITH CHECK CHECK CONSTRAINT ALL;

ALTER TABLE PFSALCMP WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE STURMADISC WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SPLETIVO WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE GINTEGRACAO WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SFILIAL WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE STIPOCURSO WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SPROFESSOR WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE STITULACAO WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE STURMA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SPROFESSORTURMA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE VNIVEISTABSALARIAIS WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE VTABELASALARIAL WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE ETURMISTA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SATIVIDADEPROFESSOR WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SATIVIDADEEXTRA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SGRUPOATIVIDADE WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE STURMADISCGERENCIADA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SHORAAULA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SHABILITACAOFILIAL WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SPROFESSORFILIAL WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SATIVIDADE WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SHABILITACAOFILIALPROFESSOR WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SCONTRATO WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SMATRICULA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SHABILITACAOFILIALINTPROTHEUS WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SSTATUS WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SMATRICPL WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE SDISCIPLINA WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE PFSALCMP WITH CHECK CHECK CONSTRAINT ALL;

          ALTER TABLE PVALETR CHECK CONSTRAINT ALL;

          ALTER TABLE VENTIDADES CHECK CONSTRAINT ALL;

         ALTER TABLE PFREEMBOLSOOPERADORAMENSAL CHECK CONSTRAINT ALL;

         ALTER TABLE GUSUARIO CHECK CONSTRAINT ALL;

Atualmente é possível realizar a importação de mais de um arquivo XLB em uma base vazia quando o arquivo pertencer a outro funcionário da mesma coligada.

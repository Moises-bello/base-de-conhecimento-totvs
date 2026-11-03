---
content_hash: 7661fdb30060f98ffcc30be4aed957a450f853dc697f655bb4f86d3dac358ce2
fetched_at: '2026-06-29T00:06:14.954336+00:00'
page_id: '210050601'
product: rm
source: tdn-rm
title: FOP_DT_Validador_Base_Dados_eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/FOP_DT_Validador_Base_Dados_eSocial
version: 11
---

# VALIDADOR DE BASE DE DADOS DO eSOCIAL

## Características do Requisito

| **Linha de Produto:** | *RM* |
| --- | --- |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *eSocial* | *Validador de Base* | |
| **Versões / Release:** | Biblioteca RM 12.1.8 **|** 11.83 **|** 11.82.42 (Específica) |
|  |  |

## Descrição

Essa implementação disponibiliza ao usuário uma forma de visualizar os dados inconsistentes na base de dados para a geração dos arquivos iniciais do eSocial.

O usuário pode realizar a seleção dos eventos que deseja realizar a validação através da uma tela de *Wizard*, após a execução do processo o sistema exibe uma*view* com os resultados da validação da base de dados.

## Procedimento para Utilização

O processo de **Validador de Base do eSocial** está localizado no Menu **eSocial,** Para acessá-la deve-se utilizar a nova MDI através no menu **eSocial / Validador de Base de Dados**

Na tela de processo do Validador da Base de Dados, o usuário pode selecionar os eventos que deverão ser validados, no caso em especifico do evento **S-2100** o usuário deverá informar também a seleção de funcionário que o processo irá considerar.

Os componentes de seleção serão habilitados somente quando o *flag* correspondente ao evento S-2100 for selecionado.

Após a execução do processo do Validador da Base de Dados, o sistema exibe logo em seguida, uma *view* demostrando a real situação da base, conforme as regras de validação e obrigatoriedade definidas no layout eSocial, os resultados do processo são exibidos separadamente por abas, onde cada aba irá constar as informações de cada evento.

A aba de resumo exibe os totais das inconsistências encontradas nos eventos e o percentual de completude de cada um

A aba **Gráfico**exibe dois gráficos em que um disponibiliza o percentual de completude geral da base de dados e o outro exibe o percentual de completude por evento.

# **Erro / Ação**

# **Registros Comuns**

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpInsc' do registro 'ideEmpregador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideEmpregador / tpInsc |
| **Descrição** | Tipo de Inscrição do Empregador (Tabela 5) |
| **Instruções** | Esse campo é calculado através do preenchimento do campo Classificação Tributária. Verifique se esse campo está preenchido. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrInsc' do registro 'ideEmpregador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideEmpregador / nrInsc |
| **Descrição** | Número da Inscrição do Empregador |
| **Instruções** | Verificar o preenchimento do campo CNPJ, CPF ou CEI do cadastro de Coligadas. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cadastros Globais / Coligadas / CNPJ, CPF ou CEI |

|  |  |
| --- | --- |
| **Erro** | **Informar o Tipo de Ambiente nos Parâmetros Gerais do eSocial!** |
| **Registro / Campo** | ideEvento / tpAmb |
| **Descrição** | Tipo de Ambiente |
| **Instruções** | Verificar o preenchimento do parâmetro Tipo de Ambiente no parametrizador do eSocial. |
| **Caminho** | RH / Folha de Pagamento / Configurações / Parametrizador / 06.07 - eSocial / Etapa 1 - eSocial: Configurações Gerais / Tipo de Ambiente |

# S-1000 - Informações do Empregador/Contribuinte

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmRazao' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / nmRazao |
| **Descrição** | Nome/Razão Social |
| **Instruções** | Verificar o preenchimento do campo Nome do cadastro de Coligadas. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cadastros Globais / Coligadas / Nome |

|  |  |
| --- | --- |
| **Erro** | **O campo 'classTrib' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / classTrib |
| **Descrição** | Classificação Tributária (Tabela 8) |
| **Instruções** | Verificar o preenchimento do campo Classificação Tributária. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'natJurid' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / natJurid |
| **Descrição** | Natureza Jurídica |
| **Instruções** | Verificar o preenchimento do campo Natureza Jurídica |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Natureza Jurídica |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'natJurid': O preenchimento do campo é obrigatório e exclusivo para empregador PJ.** |
| **Registro / Campo** | infoCadastro / natJurid |
| **Descrição** | Natureza Jurídica |
| **Instruções** | Verificar se o campo referente a Classificação Tributária está preenchido com os valores '21 - Pessoa Física, exceto Segurado Especial' ou '22 - Segurado Especial', caso esteja, não deve-se preencher o campo de Natureza Jurídica. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Natureza Jurídica |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'natJurid': O preenchimento do campo é obrigatório e exclusivo para empregador PJ.** |
| **Registro / Campo** | infoCadastro / natJurid |
| **Descrição** | Natureza Jurídica |
| **Instruções** | Verificar se o campo referente a Classificação Tributária está preenchido com os valores '21 - Pessoa Física, exceto Segurado Especial' ou '22 - Segurado Especial', caso esteja, não deve-se preencher o campo de Natureza Jurídica. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Natureza Jurídica |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'natJurid': O preenchimento do campo é obrigatório e exclusivo para empregador PJ.** |
| **Registro / Campo** | infoCadastro / natJurid |
| **Descrição** | Natureza Jurídica |
| **Instruções** | Confirmar se o preenchimento do campo Classificação Tributária com o valor '85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas' está correto. Estando correto, verificar se a Natureza Jurídica preenchida está entre as opções listadas. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Natureza Jurídica |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indCoop' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / indCoop |
| **Descrição** | Indicativo de Cooperativa |
| **Instruções** | Verificar o preenchimento do campo Indicativo de Cooperativa. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Indicativo de Cooperativa |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'indCoop': Somente pode ser diferente de ZERO se natJurid for igual a 2143 e classTrib for igual a 06, 07, 99** |
| **Registro / Campo** | infoCadastro / indCoop |
| **Descrição** | Indicativo de Cooperativa |
| **Instruções** | Confirmar se o preenchimento do campo Natureza Jurídica com o valor '214-3 - Cooperativa' está correto. Caso esteja, confirmar se a Classificação Tributária está preenchida com os valores '06 - Agroindústria', '07 - Produtor Rural Pessoa Jurídica' ou '99 - Pessoa Jurídica em Geral', caso estejam, o Indicativo de Cooperativa não pode estar marcado com '0 - Não é cooperativa'. Altere esse campo para outro valor válido. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Indicativo de Cooperativa |
| **Caminhos Associados** | **Natureza Jurídica:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Natureza Jurídica  **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'indCoop': Para classTrib for igual a 06, 07 o campo deverá ser preenchido apenas com 0,2.** |
| **Registro / Campo** | infoCadastro / indCoop |
| **Descrição** | Indicativo de Cooperativa |
| **Instruções** | Confirmar se a Classificação Tributária está preenchida com os valores '06 - Agroindústria' ou '07 - Produtor Rural Pessoa Jurídica', caso estejam, o Indicativo de Cooperativa não pode estar marcado com '0 - Não é cooperativa'. Altere esse campo para outro valor válido. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Indicativo de Cooperativa |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cnaePrep' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / cnaePrep |
| **Descrição** | CNAE Preponderante |
| **Instruções** | Verificar o preenchimento do campo CNAE Preponderante. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / CNAE preponderante |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indConstr' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / indConstr |
| **Descrição** | Indicativo de Construtora |
| **Instruções** | Verificar o preenchimento do campo Indicativo de Construtora. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Indicativo de Construtora |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indDesFolha' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / indDesFolha |
| **Descrição** | Indicativo de Desoneração da Folha |
| **Instruções** | Verificar o preenchimento do campo Indicativo de Desoneração da Folha. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Indicativo de Desoneração da Folha |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'indDesFolha': Pode ser igual a 1, 2 apenas se a classificação tributária for igual a 02, 03, 99.** |
| **Registro / Campo** | infoCadastro / indDesFolha |
| **Descrição** | Indicativo de Desoneração da Folha |
| **Instruções** | Confirmar se o Indicativo de Desoneração da Folha está marcado com '1 - Empresa enquadrada no Art. 14 da Lei 11.774/2008' ou '2 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/2011', caso esteja, a Classificação Tributária deve estar preenchido com os valores '02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída', '03 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída' ou '99 - Pessoas Jurídicas em Geral'. Caso não esteja, altere o Indicativo de Desoneração da Folha ou a Classificação Tributária para outro valor válido. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Indicativo de Desoneração da Folha |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indOptRegEletronico' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / indOptRegEletronico |
| **Descrição** | Indicativo de registro eletrônico de empregados |
| **Instruções** | Verificar o preenchimento do campo Indicativo de registro eletrônico de empregados. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Indicativo de optante pelo registro eletrônico |

|  |  |
| --- | --- |
| **Erro** | **O campo 'multTabRubricas' do registro 'infoCadastro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCadastro / multTabRubricas |
| **Descrição** | Múltiplas Tabelas de Rubricas |
| **Instruções** | Para a linha RM não existe a possibilidade de múltiplas tabelas de rubricas para a mesma coligada, portanto retorna sempre o valor padrão 'N' (Não). |

|  |  |
| --- | --- |
| **Erro** | **O campo 'fap' do registro 'infoFap' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoFap / fap |
| **Descrição** | Fator Acidentário de Prevenção |
| **Instruções** | Verificar no cadastro de Valores Fixos se existe registro para o código FAP e se esse registro possui validade para a competência atual. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cálculos / Valores Fixos / Código FAP |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'fap': Deve ser um número maior ou igual a 0,5000 e menor ou igual a 2,0000** |
| **Registro / Campo** | infoFap / fap |
| **Descrição** | Fator Acidentário de Prevenção |
| **Instruções** | Verificar no cadastro de Valores Fixos no registro vigente da Alíquota FAP se o valor informado está entre 0,5000 e 2,0000. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cálculos / Valores Fixos / Código FAP |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'procAdmJudFap' é obrigatório e não está preenchido.** |
| **Registro / Campo** | procAdmJudFap / nrProc |
| **Descrição** | Número do processo que suspende ou altera a alíquota FAP (Fator Acidentário de Prevenção) |
| **Instruções** | Verificar o preenchimento do campo Número do processo. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Processo alteração alíquota FAP / Número do Processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'siglaMin' do registro 'dadosIsencao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosIsencao / siglaMin |
| **Descrição** | Ministério/Lei que concedeu o Certificado |
| **Instruções** | Confirmar se o preenchimento do campo Classificação Tributária com o valor '80 - Entidade Beneficente/Isenta' está correto. Estando correto, verificar o preenchimento do campo Ministério. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Dados da Isenção / Ministério |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrCertif' do registro 'dadosIsencao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosIsencao / nrCertif |
| **Descrição** | Número do Certificado de Entidade Beneficente de Assistência Social, número da portaria de concessão do Certificado, ou, no caso de concessão através de Lei específica, o número da Lei. |
| **Instruções** | Confirmar se o preenchimento do campo Classificação Tributária com o valor '80 - Entidade Beneficente/Isenta' está correto. Estando correto, verificar o preenchimento do campo Certificado. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Dados da Isenção / Certificado |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtEmisCertif' do registro 'dadosIsencao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosIsencao / dtEmisCertif |
| **Descrição** | Data de Emissão do Certificado/publicação da Lei |
| **Instruções** | Confirmar se o preenchimento do campo Classificação Tributária com o valor '80 - Entidade Beneficente/Isenta' está correto. Estando correto, verificar o preenchimento do campo Data de emissão do certificado. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Dados da Isenção / Data de emissão do certificado |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtVencCertif' do registro 'dadosIsencao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosIsencao / dtVencCertif |
| **Descrição** | Data de Vencimento do Certificado |
| **Instruções** | Confirmar se o preenchimento do campo Classificação Tributária com o valor '80 - Entidade Beneficente/Isenta' está correto. Estando correto, verificar o preenchimento do campo Data de vencimento do certificado. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Dados da Isenção / Data de vencimento do certificado |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtVencCertif': Não pode ser anterior a dtEmisCertif.** |
| **Registro / Campo** | dadosIsencao / dtVencCertif |
| **Descrição** | Data de Vencimento do Certificado |
| **Instruções** | Verificar o preenchimento do campo Data de vencimento do certificado e se a data informada é anterior a informada no campo Data de emissão do certificado. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Dados da Isenção / Data de vencimento do certificado |
| **Caminhos Associados** | **Data de emissão do certificado:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Dados da Isenção / Data de emissão do certificado |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmCtt' do registro 'contato' é obrigatório e não está preenchido.** |
| **Registro / Campo** | contato / nmCtt |
| **Descrição** | Nome do Contato |
| **Instruções** | Verificar o preenchimento do campo Nome do Contato. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Contato / Nome |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cpfCtt' do registro 'contato' é obrigatório e não está preenchido.** |
| **Registro / Campo** | contato / cpfCtt |
| **Descrição** | CPF do Contato |
| **Instruções** | Verificar o preenchimento do campo CPF do Contato. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Contato / CPF |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'foneFixo': preenchimento é obrigatório se o campo foneCel não for preenchido. Se preenchido, deve conter apenas números, com o mínimo de dez dígitos.** |
| **Registro / Campo** | contato / foneFixo |
| **Descrição** | Telefone Fixo do Contato |
| **Instruções** | Confirmar se os campos Telefone Fixo do Contato ou o campo Celular do Contato estão preenchidos. Ao menos um deles precisa estar preenchido. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Contato / DDD - Telefone |
| **Caminhos Associados** | **Celular do Contato:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Contato / DDD - Celular |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'email': O e-mail deve possuir o caractere "@" e este não pode estar no início e no fim do e-mail. Deve possuir no mínimo um caractere "." depois do @ e não pode estar no fim do e-mail.** |
| **Registro / Campo** | contato / email |
| **Descrição** | Endereço Eletrônico do Contato |
| **Instruções** | Verificar se o endereço eletrônico informado do campo E-mail é valido conforme regras. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Contato / E-mail |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indAcordoIsenMulta' do registro 'infoOrgInternacional' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoOrgInternacional / indAcordoIsenMulta |
| **Descrição** | Indicativo da existência de acordo internacional para isenção de  multa |
| **Instruções** | Confirmar se o preenchimento do campo Classificação Tributária com o valor '60 - Missão Diplomática ou Repartição Consular de carreira estrangeira' está correto. Estando correto, verificar o preenchimento do campo Indicativo acordo de multa. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Informações exclusivas de organismos internacionais e outras instituições extraterritoriais / Indicativo acordo de multa (Sem acordo / com acordo) |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cnpjSoftHouse' do registro 'softwareHouse' é obrigatório e não está preenchido.** |
| **Registro / Campo** | softwareHouse / cnpjSoftHouse |
| **Descrição** | CNPJ da Empresa de Software |
| **Instruções** | Confirmar que houve um cadastro de Software House e que existe vínculo nas Informações do Empregador. Estando correto, verificar o preenchimento do campo CNPJ. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Software House / CNPJ |
| **Caminhos Associados** | **Software House do empregador:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Software House do empregador |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmRazao do registro 'softwareHouse' é obrigatório e não está preenchido.** |
| **Registro / Campo** | softwareHouse / nmRazao |
| **Descrição** | Razão Social da Empresa de Software |
| **Instruções** | Confirmar que houve um cadastro de Software House e que existe vínculo nas Informações do Empregador. Estando correto, verificar o preenchimento do campo Nome ou Razão Social. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Software House / Nome ou Razão Social |
| **Caminhos Associados** | **Software House do empregador:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Software House do empregador |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmCont' do registro 'softwareHouse' é obrigatório e não está preenchido.** |
| **Registro / Campo** | softwareHouse / nmCont |
| **Descrição** | Nome do Contato da Empresa de Software |
| **Instruções** | Confirmar que houve um cadastro de Software House e que existe vínculo nas Informações do Empregador. Estando correto, verificar o preenchimento do campo Nome do Contato. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Software House / Nome do contato |
| **Caminhos Associados** | **Software House do empregador:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Software House do empregador |

|  |  |
| --- | --- |
| **Erro** | **O campo 'telefone' do registro 'softwareHouse' é obrigatório e não está preenchido.** |
| **Registro / Campo** | softwareHouse / telefone |
| **Descrição** | Telefone da Empresa de Software |
| **Instruções** | Confirmar que houve um cadastro de Software House e que existe vínculo nas Informações do Empregador. Estando correto, verificar o preenchimento do campo DDD e Telefone. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Software House / DDD - Telefone |
| **Caminhos Associados** | **Software House do empregador:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Software House do empregador |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'email': O e-mail deve possuir o caractere "@" e este não pode estar no início e no fim do e-mail. Deve possuir no mínimo um caractere "." depois do @ e não pode estar no fim do e-mail.** |
| **Registro / Campo** | softwareHouse / email |
| **Descrição** | Endereço Eletrônico da Empresa de Software |
| **Instruções** | Confirmar que houve um cadastro de Software House e que existe vínculo nas Informações do Empregador. Estando correto, verificar se o endereço eletrônico informado do campo E-mail é valido conforme regras. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Software House / E-mail |
| **Caminhos Associados** | **Software House do empregador:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Software House do empregador |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indSitPJ' do registro 'situacaoPJ' é obrigatório e não está preenchido.** |
| **Registro / Campo** | situacaoPJ / indSitPJ |
| **Descrição** | Situação pessoa jurídica |
| **Instruções** | Verificar se o campo referente a Classificação Tributária não está preenchido com os valores '21 - Pessoa Física, exceto Segurado Especial' ou '22 - Segurado Especial' e o campo Situação pessoa jurídica está preenchido. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Situação pessoa jurídica |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indSitPF' do registro 'situacaoPF' é obrigatório e não está preenchido.** |
| **Registro / Campo** | situacaoPF / indSitPF |
| **Descrição** | Situação pessoa física |
| **Instruções** | Verificar se o campo referente a Classificação Tributária está preenchido com os valores '21 - Pessoa Física, exceto Segurado Especial' ou '22 - Segurado Especial' e o campo Situação pessoa física está preenchido. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Situação pessoa física |
| **Caminhos Associados** | **Classificação Tributária:** RH / Folha de Pagamento / eSocial / Informações do Empregador / Classificação Tributária |

# S-1005 - Tabela de Estabelecimentos e Obras de Construção Civil

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpInsc' do registro 'ideEstab' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideEstab / tpInsc |
| **Descrição** | Tipo de Inscrição (Tabela 5) |
| **Instruções** | Verificar o preenchimento do campo Tipo de Lotação. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / Tipo da Lotação |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrInsc' do registro 'ideEstab' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideEstab / nrInsc |
| **Descrição** | Número de Inscrição do Estabelecimento |
| **Instruções** | Verificar se o campo referente ao Tipo de Lotação está preenchido com os valores '01 - Setor, departamento, estabelecimento ou conjunto de estabelecimentos do contribuinte, inclusive administração, no caso de cooperativa de trabalho, e dependências do próprio trabalhador (trabalho remoto)', '04 - Pessoa Jurídica Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991', '05 - Pessoa Jurídica Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta', '06 - Entidade beneficente/isenta Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho','08 - Operador Portuário' ou '09 - Empresa Contratante de Avulsos não portuários por intermédio do Sindicato', caso esteja, verificar o preenchimento do campo CNPJ. Caso o Tipo de Lotação esteja preenchido com os valores '02 - Obra Própria - Pessoa Jurídica', '03 - Obra de Construção Civil (Empreitada Parcial ou Subempreitada)' ou '22 - Obra Própria - Pessoa Física', verificar o preenchimento do campo CNO da obra própria. |
| **Caminho** | **CNPJ:** RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / CNPJ  **CNO da obra própria:** RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / CNO da obra própria |
| **Caminhos Associados** | **Tipo da Lotação:** RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / Tipo da Lotação |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cnaePrep' do registro 'dadosEstab' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosEstab / cnaePrep |
| **Descrição** | Código do CNAE |
| **Instruções** | Verificar o preenchimento do campo CNAE. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / RAIS CAGED / Atividade Econômica |

|  |  |
| --- | --- |
| **Erro** | **O campo 'aliqRat' do registro 'aliqGilrat' é obrigatório e não está preenchido.** |
| **Registro / Campo** | aliqGilrat / aliqRat |
| **Descrição** | Alíquota RAT (Riscos Ambientais do Trabalho) |
| **Instruções** | Verificar o preenchimento do campo Percentual Acidente Trabalho. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Dados p INSS / Percentual Acidente Trabalho |

|  |  |
| --- | --- |
| **Erro** | **O campo 'fap' do registro 'aliqGilrat' é obrigatório e não está preenchido.** |
| **Registro / Campo** | aliqGilrat / fap |
| **Descrição** | Fator Acidentário de Prevenção |
| **Instruções** | Verificar no cadastro de Valores Fixos se existe registro para o código FAP e se esse registro possui validade para a competência atual. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cálculos / Valores Fixos / Código FAP |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'fap': Deve ser um número maior ou igual a 0,5000 e menor ou igual a 2,0000** |
| **Registro / Campo** | aliqGilrat / fap |
| **Descrição** | Fator Acidentário de Prevenção |
| **Instruções** | Verificar no cadastro de Valores Fixos no registro vigente da Alíquota FAP se o valor informado está entre 0,5000 e 2,0000. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cálculos / Valores Fixos / Código FAP |

|  |  |
| --- | --- |
| **Erro** | **O campo 'fap' do registro 'aliqGilrat' é obrigatório e não está preenchido.** |
| **Registro / Campo** | aliqGilrat / aliqRatAjust |
| **Descrição** | Alíquota do RAT após ajuste pelo FAP |
| **Instruções** | Campo é resultado da multiplicação do valor fixo FAP (Fator Acidentário de Prevenção) vigente com o valor da Alíquota RAT (Riscos Ambientais do Trabalho). Verificar o preenchimento do campo Percentual Acidente Trabalho e verificar no cadastro de Valores Fixos se existe registro para o código FAP e se esse registro possui validade para a competência atual. |
| **Caminhos Associados** | **FAP:** RH / Folha de Pagamento / Administração de Pessoal / Cálculos / Valores Fixos / Código FAP  **RAT:** RH / Folha de Pagamento / Administração de Pessoal / Seções / Dados p INSS / Percentual Acidente Trabalho |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpProc' do registro 'procAdmJudRat' é obrigatório e não está preenchido.** |
| **Registro / Campo** | procAdmJudRat / tpProc |
| **Descrição** | Tipo do processo que suspende ou altera a alíquota RAT (Riscos Ambientais do Trabalho) |
| **Instruções** | Verificar o preenchimento do campo Tipo do processo. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Processo alteração alíquota RAT / Tipo de Processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'procAdmJudRat' é obrigatório e não está preenchido.** |
| **Registro / Campo** | procAdmJudRat / nrProc |
| **Descrição** | Número do processo que suspende ou altera a alíquota RAT (Riscos Ambientais do Trabalho) |
| **Instruções** | Verificar o preenchimento do campo Número do processo. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Processo alteração alíquota RAT / Número do Processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpProc' do registro 'procAdmJudFap' é obrigatório e não está preenchido.** |
| **Registro / Campo** | procAdmJudFap / tpProc |
| **Descrição** | Tipo do processo que suspende ou altera a alíquota FAP (Fator Acidentário de Prevenção) |
| **Instruções** | Verificar o preenchimento do campo Tipo do processo. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Processo alteração alíquota FAP / Tipo de Processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'procAdmJudFap' é obrigatório e não está preenchido.** |
| **Registro / Campo** | procAdmJudFap / nrProc |
| **Descrição** | Número do processo que suspende ou altera a alíquota FAP (Fator Acidentário de Prevenção) |
| **Instruções** | Verificar o preenchimento do campo Número do processo. |
| **Caminho** | RH / Folha de Pagamento / eSocial / Informações do Empregador / Processo alteração alíquota FAP / Número do Processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indSubstPatrObra' do registro 'infoObra' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoObra / indSubstPatrObra |
| **Descrição** | Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil |
| **Instruções** | Verificar o preenchimento do campo Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / eSocial / Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil |

# S-1010 - Tabela de Rubricas

|  |  |
| --- | --- |
| **Erro** | **O campo 'codRubr' do registro 'ideRubrica' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideRubrica / codRubr |
| **Descrição** | Código da Rubrica |
| **Instruções** | Verificar o preenchimento do campo Código. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Identificação / Código |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'codRubr': O código da rubrica não pode conter a expressão "eSocial" nas 7(sete) primeiras posições.** |
| **Registro / Campo** | ideRubrica / codRubr |
| **Descrição** | Código da Rubrica |
| **Instruções** | Verificar se o código cadastrado possui o termo "eSocial" nas primeiras 7(sete) posições, se tiver, o registro do evento deverá ser excluído e recadastrado. Uma vez que não é permitida a edição desse campo no cadastro de evento. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Identificação / Código |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dscRubr' do registro 'dadosRubrica' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosRubrica / dscRubr |
| **Descrição** | Descrição da Rubrica |
| **Instruções** | Verificar o preenchimento do campo Descrição. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Identificação / Descrição |

|  |  |
| --- | --- |
| **Erro** | **O campo 'natRubr' do registro 'dadosRubrica' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosRubrica / natRubr |
| **Descrição** | Natureza da Rubrica da Folha de Pagamento (Tabela 3) |
| **Instruções** | Verificar o preenchimento do campo Natureza da Rubrica (eSocial). |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Identificação / Natureza da Rubrica (eSocial) |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpRubr' do registro 'dadosRubrica' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosRubrica / tpRubr |
| **Descrição** | Tipo de rubrica |
| **Instruções** | Verificar o preenchimento do campo Prov/Desc/Base. |
| **Caminho** | Administração de Pessoal / Eventos / Identificação / Prov Desc Base |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'ideProcessoCP' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideProcessoCP / nrProc |
| **Descrição** | Número do processo judicial de suspensão de INSS |
| **Instruções** | Verificar o preenchimento do campo Número do processo. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Inc. Proventos / Incidência INSS Suspensa / Número do processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'extDecisao' do registro 'ideProcessoCP' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideProcessoCP / extDecisao |
| **Descrição** | Extensão da Decisão/Sentença do processo judicial de suspensão de INSS |
| **Instruções** | Verificar o preenchimento do campo Extensão da Decisão/Sentença. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Inc. Proventos / Incidência INSS Suspensa / Extensão da Decisão Sentença |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'ideProcessoIRRF' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideProcessoIRRF / nrProc |
| **Descrição** | Número do processo judicial de suspensão de IRRF |
| **Instruções** | Verificar o preenchimento do campo Número do processo. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Inc. Proventos / Incidência IRRF Suspensa / Número do processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'ideProcessoFGTS' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideProcessoFGTS / nrProc |
| **Descrição** | Número do processo judicial de suspensão de FGTS |
| **Instruções** | Verificar o preenchimento do campo Número do processo. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Inc. Proventos / Incidência FGTS Suspensa / Número do processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'ideProcessoSIND' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideProcessoSIND / nrProc |
| **Descrição** | Número do processo judicial de suspensão de contribuição sindical |
| **Instruções** | Verificar o preenchimento do campo Número do processo. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Eventos / Inc. Proventos / Incidência Contribuição Sindical Suspensa / Número do processo |

# S-1020 - Tabela de Lotações Tributárias

|  |  |
| --- | --- |
| **Erro** | **O campo 'codLotacao' do registro 'ideLotacao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideLotacao / codLotacao |
| **Descrição** | Código da Lotação |
| **Instruções** | Verificar o preenchimento do campo Código. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / Código |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'codLotacao': O código atribuído não pode conter a expressão eSocial nas 7 primeiras posições.** |
| **Registro / Campo** | ideLotacao / codLotacao |
| **Descrição** | Código da Lotação |
| **Instruções** | Verificar se o código cadastrado possui o termo "eSocial" nas primeiras 7(sete) posições, se tiver, deverá executar o processo "Trocar código da seção". Caso não seja possível essa alteração, a seção deverá ser recadastrada. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / Código |
| **Caminhos Associados** | **Processos - Trocar código da seção:** RH / Folha de Pagamento / Administração de Pessoal / Seções / Processos / Trocar código da seção |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpLotacao' do registro 'dadosLotacao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosLotacao / tpLotacao |
| **Descrição** | Tipo de Lotação (Tabela 10) |
| **Instruções** | Verificar o preenchimento do campo Tipo da Lotação. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / Tipo da Lotação |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpInsc': O campo não deve ser preenchido se tpLotacao for igual a [01,07,10,24,90].** |
| **Registro / Campo** | dadosLotacao / tpInsc |
| **Descrição** | Tipo de Inscrição (Tabela 5) |
| **Instruções** | Verificar se o campo referente ao Tipo de Lotação está preenchido com os valores '01 - Setor, departamento, estabelecimento ou conjunto de estabelecimentos do contribuinte, inclusive administração, no caso de cooperativa de trabalho, e dependências do próprio trabalhador (trabalho remoto).', '07 - Pessoa Física tomadora de Serviços prestados por Cooperados por intermédio de Cooperativa de Trabalho', '10 - Embarcação inscrita no Registro Especial Brasileiro (REB)', '24 - Residência/Outros do Empregador Doméstico' ou '90 - Lotação fora do País.', caso esteja, não deve retornar valor para o Tipo de Inscrição. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação / Tipo da Lotação |

|  |  |
| --- | --- |
| **Erro** | **O campo 'fpas' do registro 'fpasLotacao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | fpasLotacao / fpas |
| **Descrição** | Código FPAS (Tabela 4) |
| **Instruções** | Verificar o preenchimento do campo F.P.A.S. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Dados p INSS / F.P.A.S. |

|  |  |
| --- | --- |
| **Erro** | **O campo '****codTercs' do registro 'fpasLotacao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | fpasLotacao / codTercs |
| **Descrição** | Código de Terceiros (Tabela 4) |
| **Instruções** | Verificar o preenchimento do campo Cód. Terceiros (INSS). |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Dados p INSS / Cód. Terceiros (INSS) |

|  |  |
| --- | --- |
| **Erro** | **O campo 'codTerc' do registro 'procJudTerceiro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | procJudTerceiro / codTerc |
| **Descrição** | Código de Terceiros (Tabela 4) |
| **Instruções** | Verificar o preenchimento do campo Cód. Terceiro no anexo de Processo Judicial de Terceiros e Outras Entidades. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Anexos / Processo Judicial de Terceiros e Outras Entidades / Cód. Terceiro |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProcJud' do registro 'procJudTerceiro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | procJudTerceiro / nrProcJud |
| **Descrição** | Número do Processo Judicial de Terceiros |
| **Instruções** | Verificar o preenchimento do campo Número Processo Judicial no anexo de Processo Judicial de Terceiros e Outras Entidades. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Anexos / Processo Judicial de Terceiros e Outras Entidades / Número Processo Judicial |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpInscContrat' do registro 'infoEmprParcial' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoEmprParcial / tpInscContrat |
| **Descrição** | Tipo de Inscrição do contratante |
| **Instruções** | Verificar o preenchimento do campo Tipo de Inscrição. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Contratante / Tipo de Inscrição |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpInscContrat': Deve ser igual a 1 CNPJ ou 2 CPF** |
| **Registro / Campo** | infoEmprParcial / tpInscContrat |
| **Descrição** | Tipo de Inscrição do contratante |
| **Instruções** | Verificar se o campo Tipo de Inscrição está marcado com as opções permitidas: '1 - CNPJ' e '2 - CPF'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Contratante / Tipo de Inscrição |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrInscContrat' do registro 'infoEmprParcial' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoEmprParcial / nrInscContrat |
| **Descrição** | Número de Inscrição (CNPJ/CPF) do Contrante |
| **Instruções** | Verificar o preenchimento do campo Número de Inscrição. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Contratante / Número de Inscrição |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'nrInscContrat': Deve ser um número de CNPJ ou CPF válido, conforme definido em InscContrat** |
| **Registro / Campo** | infoEmprParcial / nrInscContrat |
| **Descrição** | Número de Inscrição (CNPJ/CPF) do Contratante |
| **Instruções** | Verificar se o campo Número de Inscrição foi preenchido com um CNPJ válido, caso o Tipo de Inscrição definido foi '1 - CNPJ', ou com um CPF válido, caso o Tipo de Inscrição definido foi '2 - CPF'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Contratante / Número de Inscrição |
| **Caminhos Associados** | **Tipo de Inscrição:** RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Contratante / Tipo de Inscrição |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpInscProp' do registro 'infoEmprParcial' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoEmprParcial / tpInscProp |
| **Descrição** | Tipo de Inscrição do proprietário do CNO |
| **Instruções** | Verificar o preenchimento do campo Tipo de Inscrição. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Proprietário / Tipo de Inscrição |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpInscProp': Deve ser igual a 1 CNPJ ou 2 CPF** |
| **Registro / Campo** | infoEmprParcial / tpInscProp |
| **Descrição** | Tipo de Inscrição do proprietário do CNO |
| **Instruções** | Verificar se o campo Tipo de Inscrição está marcado com as opções permitidas: '1 - CNPJ' e '2 - CPF'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Proprietário / Tipo de Inscrição |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrInscProp' do registro 'infoEmprParcial' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoEmprParcial / nrInscProp |
| **Descrição** | Número de Inscrição (CNPJ/CPF) do proprietário do CNO |
| **Instruções** | Verificar o preenchimento do campo Número de Inscrição. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Proprietário / Número de Inscrição |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'nrInscProp': Deve ser um número de CNPJ ou CPF válido, conforme definido em tpInscProprietario** |
| **Registro / Campo** | infoEmprParcial / nrInscProp |
| **Descrição** | Número de Inscrição (CNPJ/CPF) do proprietário do CNO |
| **Instruções** | Verificar se o campo Número de Inscrição foi preenchido com um CNPJ válido, caso o Tipo de Inscrição definido foi '1 - CNPJ', ou com um CPF válido, caso o Tipo de Inscrição definido foi '2 - CPF'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Proprietário / Número de Inscrição |
| **Caminhos Associados** | **Tipo de Inscrição:** RH / Folha de Pagamento / Administração de Pessoal / Seções / Identificação do Contratante / Informações do Proprietário / Tipo de Inscrição |

# S-1030 - Tabela de Cargos/Empregos Públicos

|  |  |
| --- | --- |
| **Erro** | **O campo 'codCargo' do registro 'ideCargo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideCargo / codCargo |
| **Descrição** | Código do Cargo |
| **Instruções** | Verificar o preenchimento do campo Código. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cargos Funções / Funções / Código |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmCargo' do registro 'dadosCargo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosCargo / nmCargo |
| **Descrição** | Nome do Cargo |
| **Instruções** | Verificar o preenchimento do campo Nome. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cargos Funções / Funções / Nome |

|  |  |
| --- | --- |
| **Erro** | **O campo 'codCBO' do registro 'dadosCargo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosCargo / codCBO |
| **Descrição** | Classificação Brasileira de Ocupação - CBO |
| **Instruções** | Verificar o preenchimento do campo CBO 2002. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Cargos Funções / Funções / CBO 2002 |

# S-1050 - Tabela de Horários/Turnos de Trabalho

|  |  |
| --- | --- |
| **Erro** | **O campo 'codHorContrat' do registro 'ideHorContratual' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideHorContratual / codHorContrat |
| **Descrição** | Código do Horário |
| **Instruções** | Verificar se o preenchimento do campo Código do Horário, para Horários por Intervalo ou o campo Código para Horário por Jornada. |
| **Caminhos Associados** | **Horários por Intervalo**: RH / Automação de Ponto / Cadastros / Horários por Intervalo / Código do Horário  **Horários por Jornada**: RH / Automação de Ponto / Cadastros / Horários por Jornada / Código |

|  |  |
| --- | --- |
| **Erro** | **O campo 'hrEntr' do registro 'dadosHorContratual' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosHorContratual / hrEntr |
| **Descrição** | Horário de Entrada |
| **Instruções** | Verificar o horário de Saída informado no último intervalo cadastrado. |
| **Caminho** | RH / Automação de Ponto / Cadastros / Horários por Intervalo / Jornada / Primeiro intervalo - Entrada |

|  |  |
| --- | --- |
| **Erro** | **O campo 'hrSaida' do registro 'dadosHorContratual' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosHorContratual / hrSaida |
| **Descrição** | Horário de Saída |
| **Instruções** | Verificar o horário de entrada informado no primeiro intervalo cadastrado. |
| **Caminho** | RH / Automação de Ponto / Cadastros / Horários por Intervalo / Jornada / Último intervalo - Saída |

|  |  |
| --- | --- |
| **Erro** | **O campo 'durInterv' do registro 'horarioIntervalo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | horarioIntervalo / durInterv |
| **Descrição** | Duração do Intervalo |
| **Instruções** | Verificar os campos entrada e saída do intervalo. O valor é calculado através da expressão: Saída Intervalo - Entrada Intervalo. |
| **Caminhos Associados** | **Entrada intervalo**: RH / Automação de Ponto / Cadastros / Horários por Intervalo / Jornada / Entrada intervalo  **Saída intervalo**: RH / Automação de Ponto / Cadastros / Horários por Intervalo / Jornada / Saída intervalo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'iniInterv' do registro 'horarioIntervalo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | horarioIntervalo / iniInterv |
| **Descrição** | Horário de Entrada do Intervalo |
| **Instruções** | Verificar o horário de Saída informado no intervalo cadastrado. |
| **Caminho** | RH / Automação de Ponto / Cadastros / Horários por Intervalo / Jornada / Entrada intervalo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'termInterv' do registro 'horarioIntervalo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | horarioIntervalo / termInterv |
| **Descrição** | Horário de Saída do Intervalo |
| **Instruções** | Verificar o horário de entrada informado no intervalo cadastrado. |
| **Caminho** | RH / Automação de Ponto / Cadastros / Horários por Intervalo / Jornada / Saída intervalo |

# S-1070 - Tabela de Processos Administrativos/Judiciais

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpProc' do registro 'ideProcesso' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideProcesso / tpProc |
| **Descrição** | Tipo de Processo |
| **Instruções** | Verificar o preenchimento do campo Tipo do Processo. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Tipo do Processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProc' do registro 'ideProcesso' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideProcesso / nrProc |
| **Descrição** | Número do Processo |
| **Instruções** | Verificar o preenchimento do campo Nº do Processo. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Nº do Processo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indSusp' do registro 'dadosProcesso' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosProcesso / indSusp |
| **Descrição** | Indicativo de suspensão da exigibilidade |
| **Instruções** | Verificar o preenchimento do campo Indicativo de Decisão. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Indicativo de Decisão |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtDecisao' do registro 'dadosProcesso' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosProcesso / dtDecisao |
| **Descrição** | Data da Decisão |
| **Instruções** | Verificar o preenchimento do campo Data da Decisão. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Data da Decisão |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indDeposito' do registro 'dadosProcesso' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosProcesso / indDeposito |
| **Descrição** | Indicativo de Depósito do Montante Integral |
| **Instruções** | Verificar o preenchimento do campo Depósito do Montante Integral. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Depósito do Montante Integral |

|  |  |
| --- | --- |
| **Erro** | **O campo 'ufVara' do registro 'dadosProcJud' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosProcJud / ufVara |
| **Descrição** | UF da Seção Judiciária |
| **Instruções** | Verificar o preenchimento do campo Vara e se o registro indicado está com o campo Município preenchido. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Vara |
| **Caminhos Associados** | **Município:** RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Varas / Município |

|  |  |
| --- | --- |
| **Erro** | **O campo 'codMunic' do registro 'dadosProcJud' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosProcJud / codMunic |
| **Descrição** | Código do Município Seção Judiciária |
| **Instruções** | Verificar o preenchimento do campo Vara e se o registro indicado está com o campo Município preenchido. Verificar o preenchimento do parâmetro Conceito de Classificação para Códigos de Municípios no parametrizador do eSocial. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Vara |
| **Caminhos Associados** | **Município:** RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Varas / Município  **Parametrizador:** RH / Folha de Pagamento / Configurações / Parametrizador / 06.07 - eSocial / Etapa 4 - eSocial: De-Para de Endereço / Conceito de Classificação para Códigos de Municípios |

|  |  |
| --- | --- |
| **Erro** | **O campo 'idVara' do registro 'dadosProcJud' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosProcJud / idVara |
| **Descrição** | Código de Identificação da Vara |
| **Instruções** | Verificar o preenchimento do campo Vara e se o registro indicado está com o campo Código preenchido. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Vara |
| **Caminhos Associados** | **Código:** RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Varas / Código |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indAutoria' do registro 'dadosProcJud' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dadosProcJud / indAutoria |
| **Descrição** | Indicação da Autoria |
| **Instruções** | Verificar o preenchimento do campo Autor da Ação. |
| **Caminho** | RH / Gestão de Pessoas / Gestão Organizacional / Processos Jurídicos / Processos Jurídicos / Autor da Ação (Própria empresa / Outra entidade) |

# S-2100 - Cadastramento Inicial do Vínculo

|  |  |
| --- | --- |
| **Erro** | **O campo 'cpfTrab' do registro 'trabalhador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabalhador / cpfTrab |
| **Descrição** | CPF do Trabalhador |
| **Instruções** | Verificar o preenchimento do campo CPF. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / CPF |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'cpfTrab': CPF inválido!** |
| **Registro / Campo** | trabalhador / cpfTrab |
| **Descrição** | CPF do Trabalhador |
| **Instruções** | Verificar se o campo CPF foi preenchido com um valor válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / CPF |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nisTrab' do registro 'trabalhador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabalhador / nisTrab |
| **Descrição** | NIS (PIS, PASEP ou NIT) |
| **Instruções** | Verificar o preenchimento do campo Nro. PIS PASEP. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Nro. PIS PASEP |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'nisTrab': Número de inscrição do segurado inválido!** |
| **Registro / Campo** | trabalhador / nisTrab |
| **Descrição** | NIS (PIS, PASEP ou NIT) |
| **Instruções** | Verificar se o campo Nro. PIS PASEP foi preenchido com um valor válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Nro. PIS PASEP |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmTrab' do registro 'trabalhador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabalhador / nmTrab |
| **Descrição** | Nome do Trabalhador |
| **Instruções** | Verificar o preenchimento do campo Nome. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Nome |

|  |  |
| --- | --- |
| **Erro** | **O campo 'sexo' do registro 'trabalhador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabalhador / sexo |
| **Descrição** | Sexo do Trabalhador |
| **Instruções** | Verificar o preenchimento do campo Sexo. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Sexo |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'sexo': Sexo inválido!** |
| **Registro / Campo** | trabalhador / sexo |
| **Descrição** | Sexo do Trabalhador |
| **Instruções** | Verificar se o campo Sexo foi preenchido com um valor válido [ M - Masculino | F - Feminino ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Sexo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'racaCor' do registro 'trabalhador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabalhador / racaCor |
| **Descrição** | Raça e cor do trabalhador |
| **Instruções** | Verificar o preenchimento do campo Cor/Raça. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Cor Raça |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'racaCor': Valores Válidos: 1,2,4,6,8,9** |
| **Registro / Campo** | trabalhador / racaCor |
| **Descrição** | Raça e cor do trabalhador |
| **Instruções** | Verificar se o campo Cor/Raça foi preenchido com um valor válido [ '1 - Branca', '2 - Negra', '3 - Parda (parda ou declarada como mulata, cabocla, cafuza, mameluca ou mestiça de negro com pessoa de outra cor ou raça)', '4 - Amarela (de origem japonesa, chinesa, coreana etc)', '5 - Indígena' ou '6 - Não informado' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Cor Raça |

|  |  |
| --- | --- |
| **Erro** | **O campo 'estCiv' do registro 'trabalhador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabalhador / estCiv |
| **Descrição** | Estado civil do trabalhador |
| **Instruções** | Verificar o preenchimento do campo Estado Civil. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Estado Civil |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'estCiv': Valores Válidos: 1, 2, 3, 4, 5** |
| **Registro / Campo** | trabalhador / estCiv |
| **Descrição** | Estado civil do trabalhador |
| **Instruções** | Verificar se o campo Estado Civil foi preenchido com um valor válido [ '1 - Solteiro', '2 - Casado', '3 - Divorciado',  '4 - Separado' ou '5 - Viúvo' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Estado Civil |

|  |  |
| --- | --- |
| **Erro** | **O campo 'grauInstr' do registro 'trabalhador' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabalhador / grauInstr |
| **Descrição** | Grau de instrução do trabalhador |
| **Instruções** | Verificar o preenchimento do campo Grau Instrução. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Grau Instrução |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'grauInstr': Valores Válidos: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12** |
| **Registro / Campo** | trabalhador / grauInstr |
| **Descrição** | Grau de instrução do trabalhador |
| **Instruções** | Verificar se o campo Grau Instrução foi preenchido com um valor válido [ '1 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou', '2 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular', '3 - 5º ano completo do Ensino Fundamental', '4 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)', '5 - Ensino Fundamental Completo', '6 - Ensino Médio incompleto', '7 - Ensino Médio completo', '8 - Educação Superior incompleta', '9 - Educação Superior completa', '10 - Pós-Graduação completa', '11 - Mestrado completo' ou '12 - Doutorado completo' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Grau Instrução |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtNascto' do registro 'nascimento' é obrigatório e não está preenchido.** |
| **Registro / Campo** | nascimento / dtNascto |
| **Descrição** | Data de Nascimento |
| **Instruções** | Verificar o preenchimento do campo Dt. Nascimento. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Dt. Nascimento |

|  |  |
| --- | --- |
| **Erro** | **O campo 'paisNascto' do registro 'nascimento' é obrigatório e não está preenchido.** |
| **Registro / Campo** | nascimento / paisNascto |
| **Descrição** | País de nascimento do trabalhador (Tabela 6) |
| **Instruções** | Verificar o preenchimento do campo Estado Natal e o preenchimento do parâmetro Conceito de Classificação para Códigos de Países no parametrizador do eSocial. Avaliar também se houve o vínculo entre o Pais e a Codificação de País. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Estado Natal |
| **Caminhos Associados** | **Parametrizador**: RH / Folha de Pagamento / Configurações / Parametrizador / 06.07 - eSocial / Etapa 4 - eSocial: De-Para de Endereço / Conceito de Classificação para Códigos de Países  **Países**: RH / Folha de Pagamento / eSocial / Endereços / Países  **Codificação de País**: RH / Folha de Pagamento / eSocial / Endereços / País / Anexos / Codificação de País |

|  |  |
| --- | --- |
| **Erro** | **O campo 'paisNac' do registro 'nascimento' é obrigatório e não está preenchido.** |
| **Registro / Campo** | nascimento / paisNac |
| **Descrição** | País de nacionalidade do trabalhador (Tabela 6) |
| **Instruções** | Verificar o preenchimento do campo Nacionalidade e o preenchimento do parâmetro Conceito de Classificação para Códigos de Países no parametrizador do eSocial. Avaliar também se houve a atualização do Campo Nome do País no cadastro do Nações. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Nacionalidade |
| **Caminhos Associados** | **Parametrizador**: RH / Folha de Pagamento / Configurações / Parametrizador / 06.07 - eSocial / Etapa 4 - eSocial: De-Para de Endereço / Conceito de Classificação para Códigos de Países  **Classificação de Nações**: RH / Folha de Pagamento / eSocial / Endereços / Classificação de Nações / Nome Do País |
| **Erro** | **O campo 'nrCtps' do registro 'CTPS' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CTPS / nrCtps |
| **Descrição** | Número da carteira de trabalho e Previdência Social do trabalhador - CTPS |
| **Instruções** | Verificar o preenchimento do campo Nro. CTPS. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Nro. CTPS |

|  |  |
| --- | --- |
| **Erro** | **O campo 'serieCtps' do registro 'CTPS' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CTPS / serieCtps |
| **Descrição** | Número de série da CTPS |
| **Instruções** | Verificar o preenchimento do campo Série CTPS. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Série CTPS |

|  |  |
| --- | --- |
| **Erro** | **O campo 'ufCtps' do registro 'CTPS' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CTPS / ufCtps |
| **Descrição** | UF da expedição da CTPS |
| **Instruções** | Verificar o preenchimento do campo Estado CTPS. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Estado CTPS |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrRic' do registro 'RIC' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RIC / nrRic |
| **Descrição** | Número do RIC |
| **Instruções** | Verificar o preenchimento do campo Número RIC. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Número RIC |

|  |  |
| --- | --- |
| **Erro** | **O campo 'orgaoEmissor' do registro 'RIC' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RIC / orgaoEmissor |
| **Descrição** | Órgão emissor do RIC |
| **Instruções** | Verificar o preenchimento do campo Orgão Emissor RIC. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Orgão Emissor RIC |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtExped' do registro 'RIC' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RIC / dtExped |
| **Descrição** | Data da expedição do RIC |
| **Instruções** | Verificar o preenchimento do campo Data da Emissão RIC. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Data da Emissão RIC |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrRg' do registro 'RG' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RG / nrRg |
| **Descrição** | Número do RG |
| **Instruções** | Verificar o preenchimento do campo Nro. Identidade. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Nro. Identidade |

|  |  |
| --- | --- |
| **Erro** | **O campo 'orgaoEmissor' do registro 'RG' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RG / orgaoEmissor |
| **Descrição** | Órgão emissor do RG |
| **Instruções** | Verificar o preenchimento do campo Órgão Emissor Identidade. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Órgão Emissor Identidade |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtExped' do registro 'RG' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RG / dtExped |
| **Descrição** | Data da expedição do RG |
| **Instruções** | Verificar o preenchimento do campo Data de Emissão Ident. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Data de Emissão Ident. |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrRne' do registro 'RNE' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RNE / nrRne |
| **Descrição** | Número de inscrição no Registro Nacional de Estrangeiros - RNE |
| **Instruções** | Verificar o preenchimento do campo Registro Geral - RNE. Só será exibido caso o campo Nacionalidade esteja preenchido com um valor diferente de Brasileiro. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Registro Geral - RNE |
| **Caminhos Associados** | **Nacionalidade:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Nacionalidade |

|  |  |
| --- | --- |
| **Erro** | **O campo 'orgaoEmissor' do registro 'RNE' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RNE / orgaoEmissor |
| **Descrição** | Órgão emissor do RNE |
| **Instruções** | Verificar o preenchimento do campo Órgão Emissor RNE. Só será exibido caso o campo Nacionalidade esteja preenchido com um valor diferente de Brasileiro. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Órgão Emissor RNE |
| **Caminhos Associados** | **Nacionalidade:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Nacionalidade |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtExped' do registro 'RNE' é obrigatório e não está preenchido.** |
| **Registro / Campo** | RNE / dtExped |
| **Descrição** | Data da expedição do RNE |
| **Instruções** | Verificar o preenchimento do campo Data Emissão RNE. Só será exibido caso o campo Nacionalidade esteja preenchido com um valor diferente de Brasileiro. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Data Emissão RNE |
| **Caminhos Associados** | **Nacionalidade:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Nacionalidade |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrOC' do registro 'OC' é obrigatório e não está preenchido.** |
| **Registro / Campo** | OC / nrOC |
| **Descrição** | Número de Inscrição no Órgão de Classe |
| **Instruções** | Verificar o preenchimento do campo Número do Registro no Órgão de Classe. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Folha de Pagamento / Registro Profissional / Número do Registro no Órgão de Classe |

|  |  |
| --- | --- |
| **Erro** | **O campo 'orgaoEmissor' do registro 'OC' é obrigatório e não está preenchido.** |
| **Registro / Campo** | OC / orgaoEmissor |
| **Descrição** | Órgão emissor do documento do Órgão de Classe |
| **Instruções** | Verificar o preenchimento do campo Código do Órgão de Classe. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Folha de Pagamento / Registro Profissional / Código do Órgão de Classe |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtExped' do registro 'OC' é obrigatório e não está preenchido.** |
| **Registro / Campo** | OC / dtExped |
| **Descrição** | Data da expedição do documento do Órgão de Classe |
| **Instruções** | Verificar o preenchimento do campo Data de Emissão. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Folha de Pagamento / Registro Profissional / Data de Emissão |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtValid': Data de Validade deve ser posterior a Data de Expedição** |
| **Registro / Campo** | OC / dtValid |
| **Descrição** | Data de Validade do documento do Órgão de Classe |
| **Instruções** | Verificar se a data informada no campo Data de Validade é inferior à data informada no campo Data de Emissão. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Folha de Pagamento / Registro Profissional / Data de Validade |
| **Caminhos Associados** | **Data de Emissão:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Folha de Pagamento / Registro Profissional / Data de Emissão |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrRegCnh' do registro 'CNH' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CNH / nrRegCnh |
| **Descrição** | Número do Registro da Carteira Nacional de Habilitação - CNH |
| **Instruções** | Verificar o preenchimento do campo Nro. Habilitação. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Nro. Habilitação |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtExped' do registro 'CNH' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CNH / dtExped |
| **Descrição** | Data da expedição da CNH |
| **Instruções** | Verificar o preenchimento do campo Data emissão CNH. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Data emissão CNH |

|  |  |
| --- | --- |
| **Erro** | **O campo 'ufCnh' do registro 'CNH' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CNH / ufCnh |
| **Descrição** | Estado Emissor da CNH |
| **Instruções** | Verificar o preenchimento do campo Estado Emissor CNH. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Estado Emissor CNH |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtValid' do registro 'CNH' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CNH / dtValid |
| **Descrição** | Data de Validade da CNH |
| **Instruções** | Verificar o preenchimento do campo Data de Venc. Habilitação. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Data de Venc. Habilitação |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtValid': Data de Validade deve ser posterior a Data de Expedição** |
| **Registro / Campo** | CNH / dtValid |
| **Descrição** | Data de Validade da CNH |
| **Instruções** | Verificar se a data informada no campo Data de Venc. Habilitação é inferior à data informada no campo Data emissão CNH. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Data de Venc. Habilitação |
| **Caminhos Associados** | **Data emissão CNH**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Data emissão CNH |

|  |  |
| --- | --- |
| **Erro** | **O campo 'categoriaCnh' do registro 'CNH' é obrigatório e não está preenchido.** |
| **Registro / Campo** | CNH / categoriaCnh |
| **Descrição** | Categoria da CNH |
| **Instruções** | Verificar o preenchimento do campo Tipo CNH. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Tipo CNH |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'categoriaCnh': Valores Válidos: A, B, C, D, E, AB, AC, AD, AE** |
| **Registro / Campo** | CNH / categoriaCnh |
| **Descrição** | Categoria da CNH |
| **Instruções** | Verificar se o campo Tipo CNH foi preenchido com um valor válido [ 'A', 'B', 'C', 'D', 'E', 'AB', 'AC', 'AD', 'AE' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / Tipo CNH |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpLograd' do registro 'brasil' é obrigatório e não está preenchido.** |
| **Registro / Campo** | brasil / tpLograd |
| **Descrição** | Tipo de Logradouro |
| **Instruções** | Verificar o preenchimento do campo Tipo da Rua e o preenchimento do parâmetro Conceito de Classificação para Tipo de Rua no parametrizador do eSocial. Avaliar também se houve o vinculo no cadastro de Logradouro com a Codificação de Tipo de Rua. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Tipo da Rua |
| **Caminhos Associados** | **Parametrizador**: RH / Folha de Pagamento / Configurações / Parametrizador / 06.07 - eSocial / Etapa 4 - eSocial: De-Para de Endereço / Conceito de Classificação para Tipo de Rua  **Codificação de Tipo de Rua**: RH / Folha de Pagamento / eSocial / Endereços / Logradouros / Anexos / Codificação de Tipo de Rua |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dscLograd' do registro 'brasil' é obrigatório e não está preenchido.** |
| **Registro / Campo** | brasil / dscLograd |
| **Descrição** | Descrição do logradouro |
| **Instruções** | Verificar o preenchimento do campo Rua. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Rua |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrLograd' do registro 'brasil' é obrigatório e não está preenchido.** |
| **Registro / Campo** | brasil / nrLograd |
| **Descrição** | Número do logradouro |
| **Instruções** | Verificar o preenchimento do campo Número. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Número |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cep' do registro 'brasil' é obrigatório e não está preenchido.** |
| **Registro / Campo** | brasil / cep |
| **Descrição** | Código de Endereçamento Postal - CEP |
| **Instruções** | Verificar o preenchimento do campo CEP. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / CEP |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'cep': CEP inválido!** |
| **Registro / Campo** | brasil / cep |
| **Descrição** | Código de Endereçamento Postal - CEP |
| **Instruções** | Verificar o valor informado no campo CEP é válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / CEP |

|  |  |
| --- | --- |
| **Erro** | **O campo 'codMunic' do registro 'brasil' é obrigatório e não está preenchido.** |
| **Registro / Campo** | brasil / codMunic |
| **Descrição** | Código do Município |
| **Instruções** | Verificar o preenchimento do campo Cidade e o preenchimento do parâmetro Conceito de Classificação para Códigos de Municípios no parametrizador do eSocial. Avaliar também se houve o vinculo no cadastro de Municípios com a Codificação do Município. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Cidade |
| **Caminhos Associados** | **Parametrizador**: RH / Folha de Pagamento / Configurações / Parametrizador / 06.07 - eSocial / Etapa 4 - eSocial: De-Para de Endereço / Conceito de Classificação para Códigos de Municípios  **Codificação do Município**: RH / Folha de Pagamento / eSocial / Endereços / Municípios / Anexos / Codificação do Município |

|  |  |
| --- | --- |
| **Erro** | **O campo 'uf' do registro 'brasil' é obrigatório e não está preenchido.** |
| **Registro / Campo** | brasil / uf |
| **Descrição** | Unidade da Federação |
| **Instruções** | Verificar o preenchimento do campo Estado. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Estado |

|  |  |
| --- | --- |
| **Erro** | **O campo 'paisResid' do registro 'exterior' é obrigatório e não está preenchido.** |
| **Registro / Campo** | exterior / paisResid |
| **Descrição** | Código do País |
| **Instruções** | Verificar o preenchimento do campo País e o preenchimento do parâmetro Conceito de Classificação para Códigos de Países no parametrizador do eSocial. Avaliar também se houve vínculo entre o País e a Codificação de País. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / País |
| **Caminhos Associados** | **Parametrizador**: RH / Folha de Pagamento / Configurações / Parametrizador / 06.07 - eSocial / Etapa 4 - eSocial: De-Para de Endereço / Conceito de Classificação para Códigos de Países  **Codificação de País**: RH / Folha de Pagamento / eSocial / Endereços / País / Anexos / Codificação de País |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dscLograd' do registro 'exterior' é obrigatório e não está preenchido.** |
| **Registro / Campo** | exterior / dscLograd |
| **Descrição** | Descrição do logradouro |
| **Instruções** | Verificar o preenchimento do campo Rua. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Rua |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrLograd' do registro 'exterior' é obrigatório e não está preenchido.** |
| **Registro / Campo** | exterior / nrLograd |
| **Descrição** | Número do logradouro |
| **Instruções** | Verificar o preenchimento do campo Número. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Número |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmCid' do registro 'exterior' é obrigatório e não está preenchido.** |
| **Registro / Campo** | exterior / nmCid |
| **Descrição** | Nome da cidade |
| **Instruções** | Verificar o preenchimento do campo Cidade. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Cidade |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtChegada' do registro 'trabEstrangeiro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabEstrangeiro / dtChegada |
| **Descrição** | Data de chegada do trabalhador ao Brasil, em caso de estrangeiro |
| **Instruções** | Verificar o preenchimento do campo Data de Chegada ao Brasil. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Data de Chegada ao Brasil |

|  |  |
| --- | --- |
| **Erro** | **O campo 'classTrabEstrang' do registro 'trabEstrangeiro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabEstrangeiro / classTrabEstrang |
| **Descrição** | Classificação da condição do trabalhador estrangeiro no Brasil |
| **Instruções** | Verificar o preenchimento do campo Classificação da condição no Brasil. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Classificação da condição no Brasil |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'classTrabEstrang':  Valores Válidos: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12** |
| **Registro / Campo** | trabEstrangeiro / classTrabEstrang |
| **Descrição** | Classificação da condição do trabalhador estrangeiro no Brasil |
| **Instruções** | Verificar se o campo Classificação da condição no Brasil foi preenchido com um valor válido [ '1 - Visto permanente', '2 - Visto temporário', '3 - Asilado', '4 - Refugiado', '5 - Solicitante de Refúgio', '6 - Residente em país fronteiriço ao Brasil', '7 - Deficiente físico e com mais de 51 anos', '8 - Com residência provisória e anistiado, em situação irregular', '9 - Permanência no Brasil em razão de filhos ou cônjuge brasileiros', '10 - Beneficiado pelo acordo entre países do Mercosul', '11 - Dependente de agente diplomático e/ou consular de países que mantém convênio de reciprocidade para o exercício de atividade remunerada no Brasil' ou '12 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Classificação da condição no Brasil |

|  |  |
| --- | --- |
| **Erro** | **O campo 'casadoBr' do registro 'trabEstrangeiro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabEstrangeiro / casadoBr |
| **Descrição** | Casado com brasileiro(a)? |
| **Instruções** | Verificar o preenchimento do campo Cônjuge no Brasil. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Cônjuge no Brasil |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'casadoBr': Valores Válidos: S, N** |
| **Registro / Campo** | trabEstrangeiro / casadoBr |
| **Descrição** | Casado com brasileiro(a)? |
| **Instruções** | Verificar se o campo Cônjuge no Brasil foi preenchido com um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Cônjuge no Brasil |

|  |  |
| --- | --- |
| **Erro** | **O campo 'filhosBr' do registro 'trabEstrangeiro' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabEstrangeiro / filhosBr |
| **Descrição** | Trabalhador estrangeiro tem filhos brasileiros? |
| **Instruções** | Verificar o preenchimento do campo Nro. Filhos no Brasil. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Nro. Filhos no Brasil |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'filhosBr': Valores Válidos: S, N** |
| **Registro / Campo** | trabEstrangeiro / filhosBr |
| **Descrição** | Trabalhador estrangeiro tem filhos brasileiros? |
| **Instruções** | Verificar se o campo Nro. Filhos no Brasil foi preenchido com um valor maior que zero, e se seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentos Estrangeiros / Nro. Filhos no Brasil |

|  |  |
| --- | --- |
| **Erro** | **O campo 'defFisica' do registro 'infoDeficiencia' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoDeficiencia / defFisica |
| **Descrição** | Deficiência Física |
| **Instruções** | Verificar o preenchimento do campo Físico. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Físico |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'defFisica': Valores Válidos: S, N** |
| **Registro / Campo** | infoDeficiencia / defFisica |
| **Descrição** | Deficiência Física |
| **Instruções** | Verificar se o campo Físico foi marcado, e se o seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Físico |

|  |  |
| --- | --- |
| **Erro** | **O campo 'defVisual' do registro 'infoDeficiencia' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoDeficiencia / defVisual |
| **Descrição** | Deficiência visual |
| **Instruções** | Verificar o preenchimento do campo Visual. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Visual |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'defVisual': Valores Válidos: S, N** |
| **Registro / Campo** | infoDeficiencia / defVisual |
| **Descrição** | Deficiência visual |
| **Instruções** | Verificar se o campo Visual foi marcado, e se o seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Visual |

|  |  |
| --- | --- |
| **Erro** | **O campo 'defAuditiva' do registro 'infoDeficiencia' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoDeficiencia / defAuditiva |
| **Descrição** | Deficiência auditiva |
| **Instruções** | Verificar o preenchimento do campo Auditivo. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Auditivo |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'defAuditiva': Valores Válidos: S, N** |
| **Registro / Campo** | infoDeficiencia / defAuditiva |
| **Descrição** | Deficiência auditiva |
| **Instruções** | Verificar se o campo Auditivo foi marcado, e se o seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Auditivo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'defMental' do registro 'infoDeficiencia' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoDeficiencia / defMental |
| **Descrição** | Deficiência Mental |
| **Instruções** | Verificar o preenchimento do campo Mental. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Mental |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'defMental': Valores Válidos: S, N** |
| **Registro / Campo** | infoDeficiencia / defMental |
| **Descrição** | Deficiência Mental |
| **Instruções** | Verificar se o campo Mental foi marcado, e se o seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Mental |

|  |  |
| --- | --- |
| **Erro** | **O campo 'defIntelectual' do registro 'infoDeficiencia' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoDeficiencia / defIntelectual |
| **Descrição** | Deficiência Intelectual |
| **Instruções** | Verificar o preenchimento do campo Deficiente Intelectual. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Deficiente Intelectual |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'defIntelectual': Valores Válidos: S, N** |
| **Registro / Campo** | infoDeficiencia / defIntelectual |
| **Descrição** | Deficiência Intelectual |
| **Instruções** | Verificar se o campo Deficiente Intelectual foi marcado, e se o seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Deficiente Intelectual |

|  |  |
| --- | --- |
| **Erro** | **O campo 'reabReadap' do registro 'infoDeficiencia' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoDeficiencia / reabReadap |
| **Descrição** | Trabalhador é Reabilitado ou Readaptado |
| **Instruções** | Verificar o preenchimento do campo Reabilitado (BR). |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Reabilitado (BR) |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'reabReadap': Valores Válidos: S, N** |
| **Registro / Campo** | infoDeficiencia / reabReadap |
| **Descrição** | Trabalhador é Reabilitado ou Readaptado |
| **Instruções** | Verificar se o campo Reabilitado (BR) foi marcado, e se o seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Deficiente / Reabilitado (BR) |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpDep' do registro 'dependente' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dependente / tpDep |
| **Descrição** | Tipo de dependente |
| **Instruções** | Valor é definido através do preenchimento dos campos: Grau de Parentesco, Data de Nascimento e Universitário Escola Técnica 2º. Grau. Verifique o preenchimento desses campos. |
| **Caminhos Associados** | **Data de Nascimento:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Data de Nascimento  **Grau de Parentesco:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Grau de Parentesco  **Universitário Escola Técnica 2º. Grau:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Universitário Escola Técnica 2º. Grau |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpDep': Valores Válidos: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12** |
| **Registro / Campo** | dependente / tpDep |
| **Descrição** | Tipo de dependente |
| **Instruções** | Verificar se o valor retornado é um valor válido [ '1 - Cônjuge', '2 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos', '3 - Filho(a) ou enteado(a) até 21 (vinte e um) anos', '4 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 (vinte e quatro) anos', '5 - Filho(a) ou enteado(a) em qualquer idade, quando incapacitado física e/ou mentalmente para o trabalho', '6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial, até 21 (vinte e um) anos', '7 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, com idade até 24 anos, se ainda estiver cursando estabelecimento de nível superior ou escola técnica de 2º grau, desde que tenha detido sua guarda judicial até os 21 anos', '8 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial, em qualquer idade, quando incapacitado física e/ou mentalmente para o trabalho', '9 - Pais, avós e bisavós', '10 - Menor pobre, até 21 (vinte e um) anos, que crie e eduque e do qual detenha a guarda judicial', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador' ou '12 - Ex-cônjuge que Receba Pensão de Alimentos' ]. |
| **Caminhos Associados** | **Data de Nascimento:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Data de Nascimento  **Grau de Parentesco:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Grau de Parentesco  **Universitário Escola Técnica 2º. Grau:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Universitário Escola Técnica 2º. Grau |

|  |  |
| --- | --- |
| **Erro** | **Inconsistência no campo: tpDep. O tipo de dependente informado é inválido. Dados do dependente(Nome: #, Idade: #, Grau do dependente: #).** |
| **Registro / Campo** | dependente / tpDep |
| **Descrição** | Tipo de dependente |
| **Instruções** | A combinação dos campos: Grau de Parentesco, Data de Nascimento e Universitário Escola Técnica 2º. Grau. Causou uma inconsistência no retorno do Tipo de dependente. Observe a idade e o grau de parentesco informados. |
| **Caminhos Associados** | **Data de Nascimento:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Data de Nascimento  **Grau de Parentesco:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Grau de Parentesco  **Universitário Escola Técnica 2º. Grau:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Universitário Escola Técnica 2º. Grau |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nmDep' do registro 'dependente' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dependente / nmDep |
| **Descrição** | Nome do Dependente |
| **Instruções** | Verificar o preenchimento do campo Nome. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Nome |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtNascto' do registro 'dependente' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dependente / dtNascto |
| **Descrição** | Data de nascimento |
| **Instruções** | Verificar o preenchimento do campo Data de Nascimento. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Data de Nascimento |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cpfDep' do registro 'dependente' é obrigatório e não está preenchido.** |
| **Registro / Campo** | dependente / cpfDep |
| **Descrição** | CPF do Dependente |
| **Instruções** | Verificar o preenchimento do campo CPF. Obrigatório a partir de 12 anos. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / CPF |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'cpfDep': CPF inválido!** |
| **Registro / Campo** | dependente / cpfDep |
| **Descrição** | CPF do Dependente |
| **Instruções** | Verificar se o campo CPF foi preenchido com um CPF válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / CPF |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'depIRRF': Valores Válidos: S, N** |
| **Registro / Campo** | dependente / depIRRF |
| **Descrição** | Dependente para fins de dedução do IRRF |
| **Instruções** | Valor é definido através do preenchimento dos campos: Incidências - IRRF, Grau de Parentesco, Data de Nascimento e Universitário Escola Técnica 2º. Grau. Verifique se o valor retornado é válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho Associados** | **IRRF:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Incidências / IRRF  **Data de Nascimento:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Data de Nascimento  **Grau de Parentesco:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Grau de Parentesco  **Universitário Escola Técnica 2º. Grau:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Universitário Escola Técnica 2º. Grau |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'depSF': Valores Válidos: S, N** |
| **Registro / Campo** | dependente / depSF |
| **Descrição** | Dependente para fins de recebimento do benefício de salário-família |
| **Instruções** | Valor é definido através do preenchimento dos campos: Incidências - Forçar incidência de Salário Família, Grau de Parentesco, Data de Nascimento, Entregou Cartão de Vacinação e Entregou comprov. frequência escolar. Verifique se o valor retornado é válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho Associados** | **Forçar incidência de Salário Família:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Incidências / Forçar incidência de Salário Família  **Entregou Cartão de Vacinação:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Incidências / Entregou Cartão de Vacinação  **Entregou comprov. frequência escolar:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Incidências / Entregou comprov. frequência escolar  **Data de Nascimento:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Data de Nascimento  **Grau de Parentesco:** RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Dependente Pensionista / Dependentes / Identificação / Grau de Parentesco |

|  |  |
| --- | --- |
| **Erro** | **O campo 'trabAposent' do registro 'aposentadoria' é obrigatório e não está preenchido.** |
| **Registro / Campo** | aposentadoria / trabAposent |
| **Descrição** | Informação de aposentadoria do trabalhador |
| **Instruções** | Verificar o preenchimento do campo Aposentadoria. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Situação / Aposentadoria |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'trabAposent': Valores Válidos: S, N** |
| **Registro / Campo** | aposentadoria / trabAposent |
| **Descrição** | Informação de aposentadoria do trabalhador |
| **Instruções** | Verificar se o campo Aposentadoria foi marcado, e se o seu retorno foi um valor válido [ 'S-Sim' | 'N-Não' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Situação / Aposentadoria |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'fonePrinc': Número do Telefone Inválido, deve conter apenas números, com o mínimo de dez dígitos.** |
| **Registro / Campo** | contato / fonePrinc |
| **Descrição** | Telefone Principal |
| **Instruções** | Verificar se o campo Telefone I foi preenchido com um Telefone válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Telefone I |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'foneAlternat': Número do Telefone Inválido, deve conter apenas números, com o mínimo de dez dígitos.** |
| **Registro / Campo** | contato / foneAlternat |
| **Descrição** | Telefone Alternativo |
| **Instruções** | Verificar se o campo Telefone II foi preenchido com um Telefone válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Endereço Principal / Telefone II |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'emailPrinc': Endereço de e-mail invalido.** |
| **Registro / Campo** | contato / emailPrinc |
| **Descrição** | E-mail Principal |
| **Instruções** | Verificar se o campo E-Mail foi preenchido com um endereço eletrônico válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / E-Mail |

|  |  |
| --- | --- |
| **Erro** | **O campo 'matricula' do registro 'vinculo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | vinculo / matricula |
| **Descrição** | Matrícula |
| **Instruções** | Verificar o preenchimento do campo Chapa. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Chapa |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpRegPrev' do registro 'vinculo' é obrigatório e não está preenchido.** |
| **Registro / Campo** | vinculo / tpRegPrev |
| **Descrição** | Tipo de regime previdenciário |
| **Instruções** | Verificar o preenchimento do campo Tipo de regime previdenciário |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Situação / Tipo de regime previdenciário |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpRegPrev': O tipo de regime previdenciário deve conter um dos seguintes valores validos 1,2,3** |
| **Registro / Campo** | vinculo / tpRegPrev |
| **Descrição** | Tipo de regime previdenciário |
| **Instruções** | Verificar se o campo Tipo de regime previdenciário foi preenchido com um valor válido [ '1 - RGPS - Regime Geral da Previdência Social', '2 - RPPS - Regime Próprio de Previdência Social no Brasil' ou '3 - RPPE - Regime Próprio de Previdência Social no Exterior' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Situação / Tipo de regime previdenciário |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtAdm' do registro 'infoCeletista' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCeletista / dtAdm |
| **Descrição** | Data de Admissão |
| **Instruções** | Verificar o preenchimento do campo Data de Admissão. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data de Admissão |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtAdm': Data Admissão deve ser posterior a Data de Nascimento do trabalhador.** |
| **Registro / Campo** | infoCeletista / dtAdm |
| **Descrição** | Data de Admissão |
| **Instruções** | Verificar se a Dt. Nascimento informada é menor que a Data de Admissão. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data de Admissão |
| **Caminhos Associados** | **Dt. Nascimento**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Dt. Nascimento |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpAdmissao' do registro 'infoCeletista' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCeletista / tpAdmissao |
| **Descrição** | Tipo de admissão do trabalhador |
| **Instruções** | Verificar o preenchimento do campo Tipo de Admissão. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Admissão |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpAdmissao': Valores Válidos:  1, 2, 3, 4** |
| **Registro / Campo** | infoCeletista / tpAdmissao |
| **Descrição** | Tipo de admissão do trabalhador |
| **Instruções** | Verificar se o campo Tipo de Admissão foi preenchido com um valor válido [ '1 - Admissão', '2 - Transferência de empresa do mesmo grupo econômico', '3 - Transferência de empresa consorciada ou de consórcio' ou '4 - Transferência por motivo de sucessão, incorporação, cisão ou fusão' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Admissão |

|  |  |
| --- | --- |
| **Erro** | **O campo 'indAdmissao' do registro 'infoCeletista' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCeletista / indAdmissao |
| **Descrição** | Indicativo de Admissão |
| **Instruções** | Verificar o preenchimento do campo Indicativo de Admissão. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Indicativo de Admissão |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'indAdmissao': Valores Válidos:  1, 2, 3** |
| **Registro / Campo** | infoCeletista / indAdmissao |
| **Descrição** | Indicativo de Admissão |
| **Instruções** | Verificar se o campo Indicativo de Admissão foi preenchido com um valor válido [ '1 - Normal', '2 - Decorrente de Ação Fiscal' ou '3 - Decorrente de Decisão Judicial' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Indicativo de Admissão |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpRegJor' do registro 'infoCeletista' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCeletista / tpRegJor |
| **Descrição** | Regime de jornada do empregado |
| **Instruções** | Verificar no Histórico de utilização do cartão de ponto do funcionário existe registro para o Funcionário na Competência atual. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Históricos / Histórico de utilização do cartão de ponto |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpRegJor': O tipo de regime de jornada deve conter um dos seguintes valores validos 1,2,3** |
| **Registro / Campo** | infoCeletista / tpRegJor |
| **Descrição** | Regime de jornada do empregado |
| **Instruções** | Verificar se o retorno foi preenchido com um valor válido [ '1 - Submetidos a Horário de Trabalho (Cap. II da CLT)', '2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT' ou '3 - Funções especificadas no Inciso II do Art. 62 da CLT' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Históricos / Histórico de utilização do cartão de ponto |

|  |  |
| --- | --- |
| **Erro** | **O campo 'natAtividade' do registro 'infoCeletista' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCeletista / natAtividade |
| **Descrição** | Natureza da atividade |
| **Instruções** | Verificar o preenchimento do campo Tipo de Funcionário. Através desse campo é verificada a Natureza da atividade. |
| **Caminhos Associados** | **Tipo de Funcionário**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Funcionário |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'natAtividade': Valores Válidos:  1, 2** |
| **Registro / Campo** | infoCeletista / natAtividade |
| **Descrição** | Natureza da atividade |
| **Instruções** | Verificar se o retorno do campo Tipo de Funcionário foi um valor válido [ '1 - Trabalho Urbano' ou '2 - Trabalho Rural' ]. |
| **Caminhos Associados** | **Tipo de Funcionário**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Funcionário |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtBase': Data Base Invalida** |
| **Registro / Campo** | infoCeletista / dtBase |
| **Descrição** | Mês relativo à data base da categoria profissional do trabalhador |
| **Instruções** | Verificar se o valor retornado do campo Data Base é um valor entre 01 e 12. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data Base |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cnpjSindCategProf' do registro 'infoCeletista' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoCeletista / cnpjSindCategProf |
| **Descrição** | CNPJ do sindicato representativo da categoria |
| **Instruções** | Verificar o preenchimento do campo Sindicato, e se o CNPJ do seu cadastro está preenchido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Sindicato / Dados do Sindicato / Sindicato |
| **Caminhos Associados** | **CNPJ**: RH / Folha de Pagamento / Administração de Pessoal / Sindicatos / Identificação / CNPJ |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'cnpjSindCategProf': Número do CNPJ do Sindicato Representativo da Categoria Invalido.** |
| **Registro / Campo** | infoCeletista / cnpjSindCategProf |
| **Descrição** | CNPJ do sindicato representativo da categoria |
| **Instruções** | Verificar se o campo CNPJ do cadastro do sindicato foi preenchido com um valor válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Sindicato / Dados do Sindicato / Sindicato |
| **Caminhos Associados** | **CNPJ**: RH / Folha de Pagamento / Administração de Pessoal / Sindicatos / Identificação / CNPJ |

|  |  |
| --- | --- |
| **Erro** | **O campo 'opcFGTS' do registro 'fgts' é obrigatório e não está preenchido.** |
| **Registro / Campo** | fgts / opcFGTS |
| **Descrição** | Opção pelo FGTS |
| **Instruções** | Verificar o preenchimento do campo Situação do FGTS. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / FGTS e SEFIP / Situação do FGTS |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'opcFGTS': Valores Válidos: 1, 2** |
| **Registro / Campo** | fgts / opcFGTS |
| **Descrição** | Opção pelo FGTS |
| **Instruções** | Verificar se o campo Situação do FGTS foi preenchido com um valor válido [ '1 - Optante' ou '2 - Não Optante' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / FGTS e SEFIP / Situação do FGTS |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'opcFGTS': Para trabalhador admitido a partir de 04/10/1988, a Opção pelo FGTS deve ser como "Optante."** |
| **Registro / Campo** | fgts / opcFGTS |
| **Descrição** | Opção pelo FGTS |
| **Instruções** | Verificar se a Data de Admissão informada é posterior a 04/10/1988, caso seja, a Opção pelo FGTS deve ser '1 - Optante'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / FGTS e SEFIP / Situação do FGTS |
| **Caminhos Associados** | **Data de Admissão**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data de Admissão |

|  |  |
| --- | --- |
| **Erro** | **O campo '****dtOpcFGTS' do registro 'fgts' é obrigatório e não está preenchido.** |
| **Registro / Campo** | fgts / dtOpcFGTS |
| **Descrição** | Data de opção do trabalhador pelo FGTS |
| **Instruções** | Verificar o preenchimento do campo Data Opção FGTS. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / FGTS e SEFIP / Data Opção FGTS |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo '****dtOpcFGTS': A data de opção deve ser sempre igual ou posterior a data de admissão. Caso a data de admissão seja posterior a 04/10/1988, a data de opção deve ser igual à data de admissão.** |
| **Registro / Campo** | fgts / dtOpcFGTS |
| **Descrição** | Data de opção do trabalhador pelo FGTS |
| **Instruções** | Verificar se a Data de Admissão informada é posterior a 04/10/1988, caso seja, a Data de opção deve ser igual a Data de Admissão. A Data de opção deve sempre ser maior ou igual s Data de Admissão. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / FGTS e SEFIP / Data Opção FGTS |
| **Caminhos Associados** | **Data de Admissão**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data de Admissão |

|  |  |
| --- | --- |
| **Erro** | **O campo 'mtvContrat' do registro 'trabTemporario' é obrigatório e não está preenchido.** |
| **Registro / Campo** | trabTemporario / mtvContrat |
| **Descrição** | Motivo da contratação de trabalhador temporário |
| **Instruções** | Verificar o preenchimento do campo Motivo de Contratação Trabalhador Temporário. A aba Trabalhador Temporário só é exibida se o Tipo de Funcionário selecionado for 'B - Temporário com redução de encargos' ou 'F - Temporário/Comissionista'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Trabalhador Temporário / Motivo de Contratação Trabalhador Temporário |
| **Caminhos Associados** | **Tipo de Funcionário**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Funcionário |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'mtvContrat': Valores Válidos: 1, 2** |
| **Registro / Campo** | trabTemporario / mtvContrat |
| **Descrição** | Motivo da contratação de trabalhador temporário |
| **Instruções** | Verificar se o campo Motivo de Contratação Trabalhador Temporário foi preenchido com um valor válido [ '1 - Necessidade transitória de substituição de seu pessoal regular' ou '2 - Acréscimo extraordinário de serviços' ]. A aba Trabalhador Temporário só é exibida se o Tipo de Funcionário selecionado for 'B - Temporário com redução de encargos' ou 'F - Temporário/Comissionista'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Trabalhador Temporário / Motivo de Contratação Trabalhador Temporário |
| **Caminhos Associados** | **Tipo de Funcionário**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Funcionário |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpInsc' do registro 'ideTomadorServ' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideTomadorServ / tpInsc |
| **Descrição** | Tipo de Inscrição do Tomador |
| **Instruções** | Verificar o preenchimento do campo Tipo do Tomador. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Rateio Tomadores / Tipo do Tomador |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpInsc': Valores Válidos: 1, 2** |
| **Registro / Campo** | ideTomadorServ / tpInsc |
| **Descrição** | Tipo de Inscrição do Tomador |
| **Instruções** | Verificar se o campo Tipo do Tomador foi preenchido com um valor válido [ '1 - CNPJ' ou '2 - CPF' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Rateio Tomadores / Tipo do Tomador |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrInsc' do registro 'ideTomadorServ' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideTomadorServ / nrInsc |
| **Descrição** | Número de Inscrição do Tomador |
| **Instruções** | Verificar o preenchimento do campo Tomador. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Rateio Tomadores / Tomador |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'nrInsc': Número de Inscrição do Tomador de Serviço Inválido.** |
| **Registro / Campo** | ideTomadorServ / nrInsc |
| **Descrição** | Número de Inscrição do Tomador |
| **Instruções** | Verificar se no cadastro de Cliente e Fornecedor verificar se o CPF ou CNPJ foi preenchido e é válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações para o Cálculo / Rateio Tomadores / Tomador |
| **Caminhos Associados** | **CPF ou CNPJ**: RH / Folha de Pagamento / Administração de Pessoal / Cliente e Fornecedor / Identificação / CPF ou CNPJ |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cpfTrabSubst' do registro 'ideTrabSubstituido' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideTrabSubstituido / cpfTrabSubst |
| **Descrição** | CPF do Trabalhador Substituído |
| **Instruções** | Verificar o preenchimento do campo Chapa do Funcionário Substituto e se o CPF do seu respectivo cadastro está preenchido. A aba Trabalhador Temporário só é exibida se o Tipo de Funcionário selecionado for 'B - Temporário com redução de encargos' ou 'F - Temporário/Comissionista'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Trabalhador Temporário / Chapa do Funcionário Substituto |
| **Caminhos Associados** | **Tipo de Funcionário**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Funcionário  **CPF**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / CPF |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'cpfTrabSubst': CPF inválido!** |
| **Registro / Campo** | ideTrabSubstituido / cpfTrabSubst |
| **Descrição** | CPF do Trabalhador Substituído |
| **Instruções** | Verificar se o campo CPF referente ao cadastro do funcionário que foi substituído foi preenchido com um valor válido. A aba Trabalhador Temporário só é exibida se o Tipo de Funcionário selecionado for 'B - Temporário com redução de encargos' ou 'F - Temporário/Comissionista'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Trabalhador Temporário / Chapa do Funcionário Substituto |
| **Caminhos Associados** | **Tipo de Funcionário**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Funcionário  **CPF**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / CPF |

|  |  |
| --- | --- |
| **Erro** | **O campo 'matricTrabSubst' do registro 'ideTrabSubstituido' é obrigatório e não está preenchido.** |
| **Registro / Campo** | ideTrabSubstituido / matricTrabSubst |
| **Descrição** | Matrícula do Trabalhador Substituído |
| **Instruções** | Verificar o preenchimento do campo Chapa do Funcionário Substituto e se a chapa do seu respectivo cadastro está preenchida. A aba Trabalhador Temporário só é exibida se o Tipo de Funcionário selecionado for 'B - Temporário com redução de encargos' ou 'F - Temporário/Comissionista'. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Trabalhador Temporário / Chapa do Funcionário Substituto |
| **Caminhos Associados** | **Tipo de Funcionário**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Tipo de Funcionário  **CPF**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Documentação / CPF |

|  |  |
| --- | --- |
| **Erro** | **O campo 'codCargo' do registro 'infoContrato' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoContrato / codCargo |
| **Descrição** | Código do Cargo |
| **Instruções** | Verificar o preenchimento do campo Função. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Função |

|  |  |
| --- | --- |
| **Erro** | **O campo 'codCateg' do registro 'infoContrato' é obrigatório e não está preenchido.** |
| **Registro / Campo** | infoContrato / codCateg |
| **Descrição** | Código da Categoria (Tabela 1) |
| **Instruções** | Verificar o preenchimento do campo Código da Categoria. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / FGTS e SEFIP / Código da Categoria |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'codCateg': Código de categoria (103) relativa a "Aprendiz" a idade do trabalhador deve estar entre 14 e 24 anos.** |
| **Registro / Campo** | infoContrato / codCateg |
| **Descrição** | Código da Categoria (Tabela 1) |
| **Instruções** | Verificar se o valor informado no campo Código da Categoria foi '7 - Menor aprendiz - Lei nº 10.097/2000', caso seja, verificar o campo Dt. Nascimento do funcionário, uma vez que só pode retornar o código '103 - Empregado - Aprendiz' se a idade estiver entre 14 e 24 anos. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / FGTS e SEFIP / Código da Categoria |
| **Caminhos Associados** | **Dt. Nascimento**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Pessoais / Identificação / Dt. Nascimento |

|  |  |
| --- | --- |
| **Erro** | **O campo 'vrSalFx' do registro 'remuneracao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | remuneracao / vrSalFx |
| **Descrição** | Salário Fixo do Trabalhador |
| **Instruções** | Verificar o preenchimento do campo Salário no Histórico de Salários. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Históricos / Histórico Salarial / Salário |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'vrSalFx': Unidade de pagamento da parte fixa da remuneração esta selecionada com valor 7, portanto o valor do salário fixo deverá ser preenchido com zero.** |
| **Registro / Campo** | remuneracao / vrSalFx |
| **Descrição** | Salário Fixo do Trabalhador |
| **Instruções** | Verificar se o Tipo de Recebimento preenchido foi ' 7 - Não aplicável - salário exclusivamente variável', caso tenha sido, o valor do salário fixo vigente precisa ser 0 (zero). |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Históricos / Histórico Salarial / Salário |
| **Caminhos Associados** | **Tipo de Recebimento**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Salário e Jornada / Tipo de Recebimento |
| **Erro** | **O campo 'undSalFixo' do registro 'remuneracao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | remuneracao / undSalFixo |
| **Descrição** | Unidade do Salário do Trabalhador |
| **Instruções** | Verificar o preenchimento do campo Tipo de Recebimento. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Salário e Jornada / Tipo de Recebimento |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'undSalFixo': Valores Válidos: 1, 2, 3, 4, 5, 6, 7** |
| **Registro / Campo** | remuneracao / undSalFixo |
| **Descrição** | Unidade do Salário do Trabalhador |
| **Instruções** | Verificar se o campo Tipo de Recebimento foi preenchido com um valor válido [ 1 - Por Hora', '2 - Por Dia', '3 - Por Semana', '4 - Por Quinzena', '5 - Por Mês', '6 - Por Tarefa' ou '7 - Não aplicável - salário exclusivamente variável' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Salário e Jornada / Tipo de Recebimento |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dscSalVar' do registro 'remuneracao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | remuneracao / dscSalVar |
| **Descrição** | Descrição do Salário Variável |
| **Instruções** | Verificar o preenchimento do campo Descrição do Salário Variável. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Salário e Jornada / Descrição do Salário Variável |

|  |  |
| --- | --- |
| **Erro** | **O campo 'tpContr' do registro 'duracao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | duracao / tpContr |
| **Descrição** | Tipo de Contrato de Trabalho |
| **Instruções** | Verificar o preenchimento do campo Contrato com Prazo. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Contrato com Prazo |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'tpContr': Valores Válidos: 1, 2** |
| **Registro / Campo** | duracao / tpContr |
| **Descrição** | Tipo de Contrato de Trabalho |
| **Instruções** | Verificar se o campo Contrato com Prazo foi preenchido com um valor válido [ '1 - Prazo indeterminado' ou  '2 - Prazo determinado' ]. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Contrato com Prazo |

|  |  |
| --- | --- |
| **Erro** | **O campo 'dtTerm' do registro 'duracao' é obrigatório e não está preenchido.** |
| **Registro / Campo** | duracao / dtTerm |
| **Descrição** | Duração do Contrato de Trabalho |
| **Instruções** | Verificar o preenchimento do campo Data Final do Contrato. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data Final do Contrato |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtTerm': Data de termino deve ser posterior a data de admissão.** |
| **Registro / Campo** | duracao / dtTerm |
| **Descrição** | Duração do Contrato de Trabalho |
| **Instruções** | Verificar se a Data Final do Contrato informada é posterior à Data de Admissão do funcionário. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data Final do Contrato |
| **Caminhos Associados** | **Data de Admissão**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data de Admissão |

|  |  |
| --- | --- |
| **Erro** | **O campo 'cnpjSindTrab' do registro 'filiacaoSindical' é obrigatório e não está preenchido.** |
| **Registro / Campo** | filiacaoSindical / cnpjSindTrab |
| **Descrição** | CNPJ do Sindicato de Filiação |
| **Instruções** | Verificar o preenchimento do campo Sindicato. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Sindicato / Dados do Sindicato / Sindicato |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'cnpjSindTrab': CNPJ Inválido!** |
| **Registro / Campo** | filiacaoSindical / cnpjSindTrab |
| **Descrição** | CNPJ do Sindicato de Filiação |
| **Instruções** | Verificar se o campo CNPJ do cadastro de Sindicato foi preenchido com um CNPJ válido. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Sindicato / Dados do Sindicato / Sindicato |
| **Caminhos Associados** | **CNPJ**: RH / Folha de Pagamento / Administração de Pessoal / Sindicatos / Identificação / CNPJ |

|  |  |
| --- | --- |
| **Erro** | **O campo 'nrProcJud' do registro 'alvaraJudicial' é obrigatório e não está preenchido.** |
| **Registro / Campo** | alvaraJudicial / nrProcJud |
| **Descrição** | Número do Processo Judicial |
| **Instruções** | Verificar o preenchimento do campo Número do processo judicial. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rotinas Mensais e Anuais / RAIS / Número do processo judicial |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtIniAfast': Deve ser uma data igual ou posterior a data de admissão do trabalhador.** |
| **Registro / Campo** | afastamento / dtIniAfast |
| **Descrição** | Data de Afastamento |
| **Instruções** | Verificar se a Data de Afastamento informada é posterior à Data de Admissão do funcionário. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Anexos / Históricos / Histórico de Afastamentos |
| **Caminhos Associados** | **Data de Admissão**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data de Admissão |

|  |  |
| --- | --- |
| **Erro** | **Erro na validação do campo 'dtDeslig': Deve ser uma data igual ou posterior a data de admissão do trabalhador.** |
| **Registro / Campo** | desligamento / dtDeslig |
| **Descrição** | Data de Desligamento |
| **Instruções** | Verificar se a Data de Desligamento informada é posterior à Data de Admissão do funcionário. |
| **Caminho** | RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Rescisão / Rescisão / Data de Desligamento |
| **Caminhos Associados** | **Data de Admissão**: RH / Folha de Pagamento / Administração de Pessoal / Funcionários / Informações Contratuais / Registro / Data de Admissão |

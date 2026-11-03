---
content_hash: 4f01d5c23375bf00f6682e938f4dae84e89d152c618f4ab94c22286da70bc679
fetched_at: '2026-06-29T00:09:22.686677+00:00'
page_id: '422546010'
product: rm
source: tdn-rm
title: Certificado Digital
type: documentation
url: https://tdn.totvs.com/display/LRM/Certificado+Digital
version: 18
---

11Importar Certificado Digitalfalse

Este cadastro possibilita a importação, edição e exclusão de certificados digitais diretamente no TOTVS Gestão Fiscal.

Para habilitar o novo menu, acesse: Serviços Globais | Segurança | Perfil.

Na tela de Edição de perfil do TOTVS Gestão Fiscal clicar na aba Acesso a Menus e selecionar a permissão Certificado Digital em Gestão Fiscal | Cadastros | Específicos | Globais (01.02.02.11)

Para importar um novo certificado digital, localize o menu Cadastros | Globais | Mais... | Certificado Digital. Na visão, inicie o processo "Importar certificado digital". Nesta etapa deve ser informado o diretório onde se localiza o arquivo do certificado digital, além de sua senha e descrição. Desta forma, o usuário terá controle de seus certificados, podendo excluí-los quando precisar e também marcá-los como ativos ou inativos no sistema.

**Observação:** Os campos validade e CNPJ (com exceção do certificado .CRT) serão preenchidos automaticamente durante a importação do certificado e não poderão ser alterados pelo usuário. O campo descrição será preenchido pelo usuário durante a importação do certificado, podendo ser alterado após a importação. O certificado sempre será importado com a opção "Ativo" marcada. Caso o usuário necessite desativar o certificado para que o mesmo não seja mais considerado no sistema, basta editá-lo e desmarcar esta opção. O arquivo do certificado digital a ser importado deve sempre estar nas extensões .PFX, .P12 ou .CRT (específico para processo de registro online de boletos no módulo TOTVS Gestão Financeira). Caso precise, o usuário também poderá excluir quaisquer certificados que forem importados, estando ativos ou não. Caso o diretório onde se encontra o arquivo seja um diretório de rede, o usuário precisa ter permissão nesse diretório para que a importação aconteça com sucesso.  
A aquisição do certificado é de inteira responsabilidade do usuário.

**Atenção!! Este cadastro suporta somente os certificados do tipo A1.**

A senha inserida pelo usuário no momento da importação do certificado, é criptografada e não será possível alterá-la após a importação. O Banco de dados não terá conhecimento da senha fornecida.

2Atualização de Certificados Digitais em Lote para Filiaisfalse

Este processo possibilita atualizar o Certificado digital de várias Filiais ao mesmo tempo diretamente no TOTVS Gestão Fiscal.

Para habilitar o novo menu, acesse: Serviços Globais | Segurança | Perfil.

Na tela de Edição de perfil do TOTVS Gestão Fiscal clicar na aba Acesso a Menus e selecionar a permissão Certificado Digital em Gestão Fiscal | Cadastros | Específicos | Globais [01.02.02.11.04]

Para utilizar a implementação basta abrir o Cadastro de Certificados Digitais, escolher o Certificado Digital desejado e selecionar a opção Processos | Atualização de Certificado Digital em Lote para Filiais

Imagem

O processo de atualização em lote consiste em:

Selecionar para qual o tipo de processo o Certificado Digital será atualizado, sendo eles:

* NF-E
* CT-e
* REINF

Selecionar as Filiais que terão o Certificado Digital atualizado (serão apresentadas na lista apenas as Filias da Coligada atual)

Pode ser usada a opção **Todos** para selecionar todas as filiais.

Imagem

Este processo inclui a reconfiguração automática do certificado no TSS independentemente da validade do certificado existente no TSS.

Durante a Atualização de Certificado Digital em Lote para Filiais, serão acionados os *web services*: **SPEDADM** e **SPEDCFGNFE** do TSS.

Estes serviços são chamados sequencialmente para cada filial e tipo processo selecionado. A execução ocorre independentemente da validade prévia do certificado no TSS, priorizando sincronização completa.

Em erros de reconfiguração, *logs* de *warning* registram filial, tipo processo, ID do certificado e mensagem do TSS/RM para diagnóstico rápido, sem impedir o fluxo do processo de Atualização de Certificado Digital em Lote para Filiais.

* SPEDADM - Administração Geral: Este *web service* gerencia a inicialização e configuração básica da empresa no TSS. Prepara o ambiente TSS antes da carga do certificado, assegurando compatibilidade com processos federais e municipais.
* SPEDCFGNFE - Configuração de Certificado: Responsável pela carga e configuração do certificado digital, além de parâmetros operacionais por tipo de documento.

Observações

* Deverá ser selecionado apenas um certificado por vez para que seja realizada a execução do processo de Atualização de Certificado Digital em Lote para Filiais.
* Já na execução do processo deve ser selecionado ao menos:
  + um tipo de processo NF-e, CT-e ou Reinf;
  + uma Filial;

Disponível a partir da Biblioteca 12.1.33

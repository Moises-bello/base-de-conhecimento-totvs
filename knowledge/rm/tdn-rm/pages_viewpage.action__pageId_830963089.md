---
content_hash: 7ec4e4f84355eb52848450dba96919af155e675251ce8a24f0413f911af5cbec
fetched_at: '2026-06-29T00:11:49.361278+00:00'
page_id: '830963089'
product: rm
source: tdn-rm
title: FGTS Digital - Arquivo Simplificado para recomposição do histórico do vínculo
  do trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=830963089
version: 34
---

false

**A partir das Versões:**

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esta funcionalidade tem como objetivo proporcionar uma melhor experiência aos nossos usuários, permitindo a geração do **ARQUIVO SIMPLIFICADO PARA RECOMPOSIÇÃO DO HISTÓRICO DO VÍNCULO DO TRABALHADOR**, seguindo o leiaute estabelecido pelo governo na [VERSÃO 1.1 – 01/03/2024](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/fgts-digital-leiaute-arquivo-recomposicao-historico-do-vinculo).

## **02. EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

1) Acesse o menu Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com TAF | Outros parâmetros OU Configurações | Parametrizador | eSocial | Configurações Gerais | Integração com Middleware | Outros parâmetros.

Para utilização do relatório, é necessário **informar o servidor e a porta** que serão utilizados para a execução desses serviços.

**Servidor/Porta API**: Servidor e porta onde o serviço de API"s RM está sendo executado. (**APiPort** do Host RM. No caso onde a ApiPort não foi discriminada nas configurações do Host, utilizar a HttpPort).   
**Servidor/Porta APP:** Servidor e porta onde o aplicativo THF está sendo executado. (Caso o servidor seja o Host RM, informar a **HttpPort**).

Para maiores informações sobre a configuração da **HttpPort** e **ApiPort**, acesse: [O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-RM-Integra%C3%A7%C3%B5es-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-).

**OBSERVAÇÃO: Se estiver executando o RM.Host.exe, o mesmo deve ser executado com administrador.**

2) Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em Acesso a Menus e permita o acesso 07.02.03.03 - Arquivo FGTS Digital

true2FGTS DigitalFGTS Digital

Acesse o menu Encargos | FGTS | Arquivo FGTS Digital, para que seja apresentada a tela com o menu para a geração do arquivo:

Na nova tela, você encontrará o menu para acessar a tela de geração do Arquivo de Recomposição de Vínculo Empregatício. Insira os campos obrigatórios para a geração e clique em "Aplicar Filtros".

| Campo | Obrigatoriedade | Descrição |
| --- | --- | --- |
| **Data Desligamento De** | Obrigatório | Informar a data de desligamento inicial para filtrar os funcionários demitidos. |
| **Data Desligamento Até** | Obrigatório | Informar a data de desligamento final para filtrar os funcionários demitidos. |
| **Estabelecimento** | Obrigatório | Clique no ícone, para listar todas as filiais que estão ativas (GFILIAL.ATIVO), e filtrar se necessário. |
| **Matrícula** | Opcional | Digite a matrícula eSocial desejada. |

## Processamento

Após aplicar os filtros, a tela seguinte será apresentada:

| Campo | Campo do Sistema |
| --- | --- |
| **CNPJ/CPF Empregador** | GCOLIGADA.CGC (RAIZ) |
| **CPF trabalhado** | PPESSOA.CPF |
| **Dt. Admissão** | PFUNC.DATAADMISSAO |
| **Matrícula** | PFUNC.MATRICULAESOCIAL |
| **Categoria TSVE** | PFHSTCATEGORIAESOCIAL.CODCATEGORIAESOCIAL Se não houver histórico, será utilizado o campo PFUNC.CODCATEGORIAESOCIAL. |

| Campo | Campo do Sistema |
| --- | --- |
| **Competência** | PFPERFF.MESCOMP e PFPERFF.ANOCOMP |
| **Categoria** | PFUNC.CODCATEGORIAESOCIAL |
| **Valor\_principal** | PFPERFF.BASEFGTS |
| **Valor\_13\_salario** | PFPERFF.BASEFGTS13 |
| **Ind\_ausencia\_FGTS** | Se não houver valor nos campos "**Valor\_principal**" e "**Valor\_13\_salario**", será gerado como "S". |

falseImportante!

* O sistema trará informações dos campos de base até a entrada do FGTS DIGITAL, que corresponde até o dia 29/02/2024.
* Serão considerados todos os funcionários demitidos, com exceção dos funcionários com tipo de demissão igual "**5-Transferência sem ônus p/ Cedente".**
* Os valores são retirados da ficha financeira. Se houver valores na ficha financeira complementar, eles devem ser restaurados para a geração do relatório.
* Quando o funcionário possuir múltiplos vínculos e houver desligamento em ambos, será gerada uma linha para cada vínculo.

## Filtros Avançados

No campo "Filtros Avançados", é possível gerar o relatório por matrícula do eSocial.

3Geração do ArquivoGeração do Arquivo

Após a aplicação dos filtros, um botão para exportar é exibido. Clique em "**Exportar | Download TXT**".

Após clicar em Exportar | Download TXT, clique em "Abrir Arquivo".

Será gerado um arquivo em formato .TXT seguindo as regras do leiaute:

Após aplicar os filtros, um botão para exportar é exibido. Clique em "**Exportar | Download CSV**".

Após clicar em Exportar | Download CSV, você poderá abrir o arquivo gerado.

Após a aplicação dos filtros e a exportação, será gerado um arquivo em formato .CSV conforme o leiaute especificado.

falseImportante!

* O arquivo em TXT ou CSV é gerado com base nas informações da tela.
* O arquivo deve conter no máximo 5000 linhas. Caso ultrapasse esse limite, serão gerados múltiplos arquivos, cada um com no máximo 5000 linhas, para garantir o cumprimento desse limite.

## **03. TABELAS UTILIZADAS**

* PPESSOA, PFUNC, PESOCIALINSSTOTALESTAB, PFHSTCATEGORIAESOCIAL, PFPERFF.

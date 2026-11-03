---
content_hash: 65ec5a3882770c6b3999699e528eb37719af732fb7249a1180a8e8f194403acd
fetched_at: '2026-06-29T00:05:57.103079+00:00'
page_id: '162169916'
product: rm
source: tdn-rm
title: COMO FAZER - Configuração de envio de E-mail para Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=162169916
version: 3
---

Produto

**RMLabore**

Processo: **Configuração de envio de E-mail para Funcionário**

Versão: 11.5X ou superior

Este roteiro visa auxiliar na parametrização do TOTVS Folha de pagamento para envio de e-mails para os funcionários cadastrados na base de dados.

1. Verifique dentro do cadastro do usuário (Cadastro | Segurança | Usuário) se existe e-mail cadastrado. Caso não tenha cadastre um e-mail valido.

Clique para visualizar imagem

2. Dentro do cadastro do funcionário deve ser cadastrado e-mail para recebimento.

Tela Delphi (Clique para visualizar imagem)Tela .Net (Clique para visualizar imagem)

3. Cadastro de e-mail global no sistema deve estar configurado corretamente. Para configurar o mesmo acessar o menu (Opções | Parâmetros | Globais). Segue link indicando modelo de configuração.

<http://tdn.totvs.com/display/public/rm/Envio+de+email+-+LINHA+RM>

4. Para enviar e-mail para funcionário, o sistema permite utilizar relatório Delphi e .NET.

5. Como exemplo iremos enviar relatório de folha de pagamento padrão do sistema. Acesse o menu (Relatório| Gerador) e edite o relatório utilizado.

**Dica:** Existe também o envio de email através do processo que se encontra em Configurações | Envia e-mails para Funcionários, veja mais detalhas no link [Enviar e-mails para Funcionários](https://tdn.totvs.com.br/pages/editpage.action?pageId=452719934)

Clique para visualizar imagem

6. Para o relatório ser gerado, o tipo do mesmo deve estar como “VISAO FUNC” e Tipo de saída como “Arquivo Bancário”

Clique para visualizar imagem

7. Para enviar e-mail basta selecionar funcionário desejado e acessar a opção (Processos | Envio de E-Mail para funcionário). Procedimento só pode ser realizado pela tela de Funcionários .NET.

Clique para visualizar imagem

8. Abrindo o menu basta avançar na primeira tela. Existe a opção de indicar e-mail para cópia.

Clique para visualizar imagem

9. Habilite a opção “Enviar relatório como Anexo”

      Selecionar o relatório que será gerado (Delphi ou .NET);

      Informar assunto para e-mail;

      Informar texto do e-mail;

Após preenchimento dos campos basta executar procedimento que contra cheque será enviado.

Clique para visualizar imagem

10. Recebimento do e-mail.

Clique para visualizar imagem

**Observações:**

**a)** O relatório utilizado no manual se trata de um exemplo. A empresa pode customizar relatório conforme necessidade para ser gerado.

**b)** No envio de e-mail, sistema reconhece filtro utilizado no relatório para gerar o mesmo. Caso no relatório esteja indicado ano, chapa, período diferente do sistema o mesmo será enviado em branco para o funcionário.

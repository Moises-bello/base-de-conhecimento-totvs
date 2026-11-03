---
content_hash: 66875fafbc6438e037b50cd07d8c6e9f6e870311a4a1b5d0dad3968e14b55d54
fetched_at: '2026-06-29T00:11:06.127635+00:00'
page_id: '63276071'
product: rm
source: tdn-rm
title: Conversor para Bases de Dados de Testes
type: documentation
url: https://tdn.totvs.com/display/LRM/Conversor+para+Bases+de+Dados+de+Testes
version: 16
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

         A funcionalidade de conversão de base de dados para teste faz com que a base possa ser utilizada para um ambiente de homologação. Após executar o conversor, a base terá seus dados alterados para dados fictícios, todos os aplicativos serão habilitados, será limitado o acesso apenas a coligada 1 e alguns processos que necessitam de CNPJ válido, não poderão ser executados, pois o objetivo é permitir o teste de novas versões e/ou aplicativos ainda não adquiridos. Por este motivo, é importante utilizar uma base de backup para executar tal procedimento. 

Importante

Após a execução desse processo, ao utilizar o sistema, licenças não serão consumidas. Nem mesmo licenças do tipo TOTVS DEV TEST na base de dados em questão, sendo assim, não há limite de usuários para acessar o sistema.

**02. EXEMPLO DE UTILIZAÇÃO**

      Converter base de dados para base de testes.

**Atividade:**

1. **Acesse:** Serviços Globais | Serviços | Banco de Dados | Conversor para Bases de Dados de Testes.

     2. Ao clicar sobre a opção aparecerá seguinte mensagem:

Clique em SIM.

3. Começara o processo de conversão.

Clique em AVANÇAR.

   4. Selecione a coligada na qual deseja ter acesso após a conversão, essa será a única coligada ativa na base e não será possível ativar outra.   
Clique em AVANÇAR.

   5. Execute.

   6. Ao clicar em Executar será questionado se deseja continuar.

Clique em SIM.

Lembre-se de **não executar** o processo em base de produção!

    7. Ao final do processo a base estará convertida para base de testes.

   8. Para confirmar a conversão, abra o cadastro de Coligadas.

**Acesse:** Serviços Globais | Administração | Cadastros | Coligada

Veja que a coligada selecionada para conversão está com o nome TESTE.

   9. Acesse também o Contexto na parte superior esquerda da tela. Clique em "Alterar contexto do módulo", em seguida clique nos três pontos.

   10. Perceba que na seleção de contexto, o único disponível é o da coligada 1.

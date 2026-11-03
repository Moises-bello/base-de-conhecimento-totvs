---
content_hash: 880393f34c38cd86fe332675c2f061a88c201ca74c88414568077153324e15b8
fetched_at: '2026-06-29T00:06:27.324734+00:00'
page_id: '232819560'
product: rm
source: tdn-rm
title: Diagnóstico do Sistema - Ferramentas de Análise de Erros - Sentinela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232819560
version: 33
---

Esta página tem por objetivo apresentar as ferramentas de análise de erros CriticalLog, ErrorReportView e Sentinela.

### **1. Critical Log**

     Esta ferramenta busca facilitar a identificação de erros críticos como por exemplo perdas momentâneas de conectividade com o banco, timeout de banco de dados e falha ao registrar algum host entre outros.

     O log exibe as as seguintes informações: Usuário conectado, nome da máquina , aplicação, informações do erro, stack trace e data do ocorrido.

     Para visualizar este log, basta acessar o diagnóstico do sistema, na aba Erros Críticos.

Auto-expurgo

O Critical Log faz expurgo dos dados à cada 2 dias. Os registros, datados em 15 dias anteriores à data de expurgo, são excluídos da tabela GCRITICALLOG.

     Criamos algumas regras para classificar um erro como crítico e alimentamos à tabela GCRITICALLOG para posterior análise, são elas:

1 – Regra com mecanismo de identificar quando o host é interrompido inesperadamente. Nesta regra quando o host é reiniciado verificamos se o mesmo seguiu o fluxo de desligamento por completo, e caso negativo geramos um registro na GCRITICALLOG com seu respectivo arquivo de dump.  
2- Regra com mecanismo de identificar queries lentas sendo executadas, sejam elas, consultas SQL ou queries de produto. Nesta regra verificamos queries que levam mais de 2 minutos para executar e geramos um registro na GCRITICALLOG.  
3 – Regra para verificar estouro de pool de conexões com o banco de dados. Nesta regra temos uma lógica de programação para identificar qual foi o processo vilão que estourou o pool de conexões, pois na maioria dos caso não é o processo que o erro foi apresentado que é o causador do problema, com isso geramos um registro na GCRITICALLOG.  
4 – Regra para identificar erros no Job Server. Nesta regra temos pontos estratégicos no fonte mapeado pelo know-how de erros para identificar configurações erradas de afinidade, de usuários do Alias, e desserialização da classe de processo, etc. Para cada erro é gerado um registro na GCRITICALLOG.  
5 – Regra para identificar sem os devidos tratamentos. Nesta regra capturamos exceções levantadas na aplicação e geramos registros na GCRITCALLOG.  
6 – Regra para calcular a recorrência. Nesta regra identificamos quais erros possuem as mesmas características e incrementamos a recorrência do mesmo.  
7 – Regra para identificar o produto. Nesta regra avaliamos o stackTrace do erro na ordem da execução e o primeiro produto encontrado é definido como o responsável pelo erro.

     Demais regras podem e serão adicionadas para que cada vez mais consigamos identificar de forma rápida erros críticos.

---

### **2. Snowden**

O Snowden é para onde todas as informações de *critical log* de clientes sobem e são compiladas de uma forma que nos permite avaliar incidentes similares de forma geral, podendo analisar os impactos em diferentes versões e em diferentes clientes.

O Endereço do Snowden é: <https://snowden.totvs.com.br/app/incidents>.

Dados para acesso:

Usuário: seuusuario@[totvs.com.br@totvs.com](mailto:totvs.com.br@totvs.com) (ex.: daniel.campos@totvs.com.br@totvs.com)  
Senha: senha de rede da TOTVS.

---

### **3. RMDbg (RM Debugger)**

       O RMDbg é uma ferramenta de análise de dump de serviços RM que nos permite fazer um diagnóstico completo do processo no momento em que o dump foi extraído. Com essa ferramenta podemos analisar eventuais vazamentos de memória, eventuais crashes de processos (*crash dump*), consultas com grande volumes de dados, relatórios com problemas e também uma série de outros fatores que podem estar comprometendo a saúde da aplicação.

      Um dump pode ser criado a qualquer momento, inclusive no ambiente de produção do cliente. Basta solicitar o time de TI do cliente, time de atendimento ou o time de Cloud de TOTVS. O material com instruções de uso e executável está [no drive](https://drive.google.com/drive/folders/1M1N6Fvx0qdMgvlyjiqpBNcVewPcj6MBi) compartilhado.

Segue exemplo de criação de dump:

---

### **4. ErrorReportView**

Com o novo recurso do relatório de erros da MDI, diversas informações que antes eram solicitadas ao cliente agora poderão ser coletadas com um único clique. Através de um novo botão disponível na janela de erros padrão, é possível para o usuário gerar um relatório contendo informações do ambiente utilizado junto a outros dados como print da tela onde o erro foi apresentado, arquivos do sistema como rm.exe. config e \_Broker.dat entre outras informações padrões.

---

### **5.** **Sentinela**

O Sentinela é uma ferramenta de Monitoramento de Ambientes criada para que o usuário possa identificar possíveis ofensores de performance. Maiores informações acesse .

Ferramentas de Diagnostico do Sistema

As ferramentas apresentadas são captadoras de diferentes não conformidades, exceções e possíveis ofensores à performance do sistema. Os dados coletados e os relatórios gerados, devem ser enviados à Totvs para que o time responsável possa analisar esses dados e relatórios e possa oferecer o suporte necessário para que as não conformidades, exceções e ofensores à performance evidenciadas sejam devidamente sanadas. Os dados das tabelas referentes à cada uma dessas funcionalidades por si só, não garantem uma análise eficiente de quaisquer problemas que possam estar ocorrendo no software ou no ambiente ao qual o software está instalado.

### **Vídeo****:**

A seguir um vídeo demonstrativo das ferramentas apresentadas:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.10 e Superiores

false

**Processo:** Ferramentas de Análise de Erros do RM

falsefalse

**Status:** Finalizado

false

**Data:** 19/04/2018

false

**Autores:**

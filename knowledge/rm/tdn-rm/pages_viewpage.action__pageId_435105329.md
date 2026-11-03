---
content_hash: b8df1848c91ffc6bbdab52115c73b04d32ee3788cac5500c6e68cdb1223adfb1
fetched_at: '2026-06-29T00:09:49.594755+00:00'
page_id: '435105329'
product: rm
source: tdn-rm
title: Atualizador da Revitalização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105329
version: 1
---

**Atualizador da Revitalização**

---

Antes de executar os scripts específicos para transformar a base padrão para revitalização é necessário que o cliente atualize a base de dados até a ultima versão de mercado liberada (12.1.9 ou superior), faça o backup desta base e execute a ferramenta "Conversor Revitalização"  
   
Acesse "Executar", localize "Conversor Revitalização"  
   
  
   
Através desta ferramenta serão executados processos que consistem os dados da base.  
Os passos devem ser executados na sequencia apresentada na tela.  
Selecione o botão de cada opção e clique em executar, este procedimento deve ser feito para todas as opções.  
   
  
   
   
A cada execução o sistema apresenta o resultado com o "Check" (verde), caso haja erro não será possível continuar até a devida correção.  
Algumas verificações podem solicitar que o usuário faça alguma correção como nos sub processos 8, 9 e 10. Nestes casos os registros que apresentarem lançamentos financeiros não integrados devem ser Efetivados ou cancelados ou ter o plano de financiamento gerado, de acordo com cada caso.  
Depois de executar todas as opções sem erros, a base estará apta para ser revitalizada. Se houver erro entre em contato com seu canal de atendimento.  
**Obs.:** Sugerimos para melhorar a performance da conversão, a reinicialização da instância do banco de dados após a execução do "Conversor da Revitalização".  
   
Para maiores informações, sobre cada etapa segue os seguintes links:   
   
Rastreamento de Lançamentos Filhos  
Conversor de Cheque Baixado  
Utilitários de Lançamento Financeiros  
Conversão dos Lançamentos Filhos para Nova Baixa  
Executar Novamente o Utilitário de Lançamentos Financeiros  
Habilitar Histórico de Lançamentos Financeiro  
Conversão dos Aditivos com XML para Tabelas (versionamento)  
Valida se existem Vendas sem Integração com Lançamento Financeiro  
Valida Vendas com Aditivos em preparação que impactam em Lanc. Financeiro  
Valida Distrato em Aberto com Plano de Financiamento gerado  
Migrar Gráficos, Relatórios e Sentenças SQL  
   
   
   
Ao final de todos os passos é preciso executar o Atualizador para versão revitalizada, para isso faça:

1. Crie um atalho do RM.Atualizador.exe
2. Clique em propriedades, campo destino, e acrescente no final do caminho o texto /beta
3. Execute o atualizador através do atalho criado, para conversão para a versão revitalizada do piloto do TIN.

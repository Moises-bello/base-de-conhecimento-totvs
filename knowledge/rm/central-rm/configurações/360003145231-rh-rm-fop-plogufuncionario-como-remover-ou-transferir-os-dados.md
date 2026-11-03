---
article_id: 360003145231
category: Configurações
content_hash: b88fe68793bd47863aa4b585f450b29f59859f4169103ecb766e9f24a45fbeb2
fetched_at: '2026-06-28T22:46:49.676955+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - PLOGUFUNCIONARIO: Como remover ou transferir os dados'
type: support-article
updated_at: '2025-03-12T09:58:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003145231-RH-RM-FOP-PLOGUFUNCIONARIO-Como-remover-ou-transferir-os-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:30min****Dúvida**Para que serve a tabela PLOGUFUNCIONARIO? Se a tabela estiver consumindo muito espaço em disco é possível limpá-la? Existe algum impacto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A tabela **PLOGFUNCIONARIO** é a responsável por guardar todos os logs de cálculo dos funcionários e por isso costuma crescer e ocupar muito espaço em disco.

Para limpar a tabela ou transferir os dados para uma tabela complementar, veja os passos abaixo:  
  
1. **Como limpar a tabela?**  
Para limpar esta tabela basta marcar o parâmetro **Remover log de cálculo de funcionários** ao liberar a competência: Acesse: **Folha mensal | Liberação de Competência**   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867881510295/mceclip0.png)  
  
O parâmetro **Remover log de cálculo de funcionários** irá excluir os logs de cálculo dos funcionários conforme parametrização específica no parametrizador em **Configurações | Parametrizador | Folha Normal | Log's**.   
  
Nesta tela será necessário informar quantos meses de logs você deseja manter na base de dados. Ou seja, se estamos no mês de Março e vamos virar competência informando 3 meses no parametrizador, o sistema irá manter os meses de Janeiro, Fevereiro e Março na base.

Assim, caso queira alterar esta parametrização, basta informar o número de meses que deseja que o sistema mantenha.  
  
2. **Como transferir para a tabela complementar?**A partir da versão **12.1.21** foi criado uma nova funcionalidade para transferir os dados da  
**PLOGFUNCIONARIO** para um tabela complementar, uma vez que esta tabela acumula muitos dados e pode influenciar no desempenho de algumas rotinas do sistema.

Essas tabelas são cópias das tabelas de cálculo originais que foram criadas para que exista a possibilidade de diminuir a carga de dados armazenadas somente nas tabelas originais.

Os logs movidos ainda podem ser acessados através do módulo de **Logs Complementares**. Uma vez que os logs tenham sido movidos para as tabelas complementares eles podem, inclusive, ser removidos da **PLOGFUNCIONARIO**.  
  
Para mover os dados, acesse **Folha Mensal | Consulta | Gerenciador de log** de cálculo e execute o processo **Mover para Logs Complementares**, conforme print abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867928706711/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8867932371095/mceclip2.png)  
  
**Saiba mais**  
[Gerenciador de log de Cálculo (Complementar)](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GerenciadorDeLogDeCalculo.aspx)

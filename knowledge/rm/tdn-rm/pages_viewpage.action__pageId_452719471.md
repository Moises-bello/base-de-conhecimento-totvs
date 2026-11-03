---
content_hash: 5443781d81602f3f8817b2740fc849cb0eb2ce0e3cd1fb7a30d8dd4bc92cc871
fetched_at: '2026-06-29T00:10:07.915024+00:00'
page_id: '452719471'
product: rm
source: tdn-rm
title: Crítica da Folha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719471
version: 2
---

Neste módulo será gerado um relatório de críticas dos eventos lançados na movimentação acumulada mensal. A crítica será feita conforme montagem de fórmulas específicas para este fim. As fórmulas de crítica servem para verificar se determinado evento foi ou não calculado para um funcionário ou grupo de funcionários.   
 O usuário poderá selecionar um funcionário digitando sua chapa ou localizando seu nome. Também será possível fazer a seleção de funcionários pela situação, tipo de funcionário e recebimento ou ainda criar Filtros, Fórmulas de Seleção, o grupo de funcionários pela seção que está cadastrado. Podendo ser informado o código de quebra da seção, quebra padrão, quebra por CNPJ (por Coligada) ou quebra por CEI.  
 **Poderão ser utilizados dois processos de crítica:**  
    
 **A execução da crítica utilizando o próprio evento deverá ser efetuada da seguinte forma:**  
    
 **1º Passo:**  
 Deverão ser cadastradas as fórmulas de mensagem de critica no módulo de tabelas dinâmicas INT 29.  
    
 **2º Passo:**  
 Crie uma fórmula crítica, informando a referência (código) da mensagem criada na tabela dinâmica.  
    
 **Exemplo:**  
    
 **Fórmula:** Critica da folha - Não descontou o adiantamento  
 SE (LI('0034') > 0) E ( C('0019') = 0)   
 ENTAO '2'  
 SENAO ''  
 FIMSE  
 **Retorno:**  
   
 Erros registrados na crítica efetuada em 04/06/2010 11:17:14  
   
 **Chapa 00001 ITAMAR MENDES DA SILVEIRA - Seção 01.03 - Situação A**  
 Fórmula 9006 = Não descontou Adiantamento Salarial  
 \*\*\*\*Onde "2" referem-se ao código das mensagens cadastradas previamente na tabela dinâmica INT 29.  
 **3º Passo:**  
 Informe no evento a referência da fórmula de crítica montada.  
 **4º Passo:**  
 Emita o relatório de crítica.  
 **Observação:**  
 Antes de emitir o relatório de crítica, certifique se o evento consta na movimentação do funcionário, caso contrário, a crítica não será realizada.  
 **A execução da crítica utilizando um conjunto de fórmulas independente do evento deverá ser efetuada da seguinte forma:**  
 **1º Passo:**  
 Cadastre as mensagens da critica no módulo de tabelas dinâmicas.  
 **2º Passo:**  
 Crie uma fórmula de crítica, informando a referência (código) da mensagem criada na tabela dinâmica.  
 **Exemplo:**  
 **Fórmula:** Critica da folha - Não tem salário família  
 SE (NDEPSF ( MTDATA (01 , MES , ANO)) = 0)   
 ENTAO '7'   
 SENAO ''   
 FIMSE  
 **Retorno:**  
 ---  
 Erros registrados na crítica efetuada em 04/06/2010 11:28:49  
 ---  
 **Chapa 00001 ITAMAR MENDES DA SILVEIRA - Seção 01.03 - Situação A**  
 Fórmula 95 = Não tem dependente para salário família  
 \*\*\*\*Onde "7" referem-se ao código das mensagens cadastradas previamente na tabela dinâmica INT 29.  
 **3º Passo:**  
 O retorno da fórmula, se não for correto, deve ser alguma mensagem já cadastrada na tabela dinâmica.  
 **4º Passo:**  
 Emita o relatório de crítica no módulo de crítica de eventos.  
 **Atenção:**  
 Após a liberação da competência a movimentação da ficha financeira complementar que foi restaurada para ficha financeira será apagada, sendo que a ficha financeira somente manterá gravada a movimentação dos últimos 25 meses considerando a competência atual, o que ultrapassar 25 meses será armazenado na ficha financeira complementar.

---
content_hash: fa9e3310ae07a6b3049378ca904443752da56422d96bde48e35f00463bd4e486
fetched_at: '2026-06-29T00:09:11.323187+00:00'
page_id: '403746916'
product: rm
source: tdn-rm
title: Processos de JOBS
type: documentation
url: https://tdn.totvs.com/display/LRM/Processos+de+JOBS
version: 14
---

# Índice

---

# Paralelização de Jobs

---

É possível realizar no sistema RM.exe a "quebra" (paralelização/divisão) de um processo em "N" processos menores quando do agendamento de um Job.   
Para paralelizar um Job, selecione um processo que deseje executar e que utilize a estrutura de JobServer, como por exemplo a geração de relatórios no RmReports.

Selecione a quantidade desejada de relatórios, acione sua geração.

Na tela que for aberta, avance. Perceba que a configuração para a escalabilidade de processos estará presente nesta tela (Agendamento de Job).

Será possível dividir o processo em "N" partes, sendo que N será <= Número de processos a serem executados,   
Exemplo: se forem selecionados 4 relatórios, N poderá ser <= 4, pois não faz sentido dividir além disso (20 partes por exemplo).

   
Um processo "leve" a ponto de não poder ser agendado também não precisará ser escalável. Dessa maneira, a opção de escalabilidade ficará desabilitada. O processo será executado, mas não dividido. A escalabilidade é possível a partir de dois processos no mínimo.  
   
Informe a quantidade de partes que deseja dividir o processo. Execute-o e perceba ao final de sua execução que o número de partes em que ele foi particionado corresponde ao número de abas abertas na tela final de execução de processos e ao número de Jobs exibidos na tela do Gerenciador de Jobs, numa determinada data/hora.

# Log do Processo

---

Na guia referente aos log´s do processo é possível verificar o resumo do processamento.

Caso algum dos processos tenha finalizado com erro, a aba correspondente à execução deste processo mostrará o ocorrido.   
Assim o usuário poderá verificar qual processo deverá corrigir e assim, agendar novamente o Job para execução.

**Observação:** Outros processos finalizados com sucesso não serão afetados por algum processo finalizado com erro.

**O editor utilizado é o Notepad.exe (Bloco de Notas) nativo do Windows.  
Para as versões:**

* **12.1.2209 até o patch 188**
* **12.1.2302 até o patch 112**

Ao clicar em bloco de notas será aberto o "notepad.exe" com o texto do log do processo.

Observação

Neste caso usando o RM em Windows 11, pode ocorrer incompatibilidade de forma que o Bloco de Notas pode abrir sem o conteúdo do Log.  
Assim será necessário usar a função de copiar e colar.

**O editor utilizado será próprio do RM, a partir das versões:**

* **12.1.2209 patch 189**
* **12.1.2302 patch 113**
* **12.1.2306 e acima**

Ao clicar no botão Abrir no Editor, o editor padrão do RM será utilizado para auxiliar na manipulação e exportação do Log do processo.  
Este editor possibilita que usuário possa formatar, imprimir e personalizar o conteúdo, disponibilizando vários formatos para salvar o Log em um arquivo.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Processos de JOBS

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

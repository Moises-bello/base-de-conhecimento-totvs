---
content_hash: 36a712bf30f2bf7c445d77904600ca11dac47bfbe75dca52cff1a3705de609d3
fetched_at: '2026-06-29T00:11:11.205333+00:00'
page_id: '64651480'
product: rm
source: tdn-rm
title: Memória insuficiente X Vemelho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64651480
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                     **Versão:**11.52 |
| **Processo** | **:** | Configurações avançadas do sistema |
| **Subprocesso** | **:** | Opções de desempenho - Memória |
| **Data da publicação** | **:** | 30/09/2013 |

Este processo permitirá configurar a memória virtual do windows de modo que a mesma realize automaticamente este gerenciamento.

Este recurso é utilizado em algumas máquinas que apresentam o **X** vermelho ao realizar acesso em algumas operações acompanhada da mensagem: **Memória insuficiente.**

# **Primeiro Passo:**

Aacesse as propreidades do **MEU COMPUTADOR**

Clique em **CONFIGURAÇÕES AVAÇADAS DO SISTEMA.**

***Selecione a opção Avançado / configurações***

Na tela seguinte, selecione o menu Avançado e escolha a opção **ALTERAR** de acordo com figura abaixo:

Nesta tela é possível definir quanto de memória será alocada para executar aplicações no Windows, nesse caso deixe sempre a opção **“Gerenciar automaticamente o tamanho do arquivo de paginação de todas as unidades”**, marcada, pois o Windows se encarregara de realizar essa paginação e alocar a quantidade de memória necessária para executar as aplicações.

# Segundo Passo

Aumente o valor da entrada de Registro IRPStackSize. Para fazer isto, execute as seguintes etapas:

1. Clique em **Iniciar**, em **Executar**, digite regedit e clique em **OK**.
2. Localize e clique na seguinte subchave do Registro:

   HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters

   Se a entrada IRPStackSize não estiver nessa subchave, execute as seguintes etapas:  
   1. Clique em **Editar**, aponte para **Novo** e clique em **Valor DWORD**.
   2. Digite IRPStackSize e pressione ENTER.   
        
      **Observação** Digite IRPStackSize exatamente como aparece. O nome do valor diferencia maiúsculas de minúsculas.
3. Clique em **IRPStackSize**, em **Editar** e em **Modificar**.
4. Na caixa **Dados do valor** digite um valor maior e clique em **OK**.  
     
   **Observação** Os valores podem ir de 0x1 a 0xC. Esses valores são equivalentes a 1 e a 12 na notação decimal.

Se o problema persistir após a conclusão do procedimento anterior, aumente o valor de IRPStackSize.

**Aviso** O uso incorreto do Editor do Registro, ou outro método, pode causar sérios problemas, que talvez exijam a reinstalação do sistema operacional. A Microsoft não garante que os problemas resultantes do uso incorreto do Editor do Registro possam ser solucionados. A modificação do Registro é de sua responsabilidade.

        FONTE:  <http://support.microsoft.com/kb/106167>

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br:11500/WikiHelp/GLB/GLB.ParametrosGlobais.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

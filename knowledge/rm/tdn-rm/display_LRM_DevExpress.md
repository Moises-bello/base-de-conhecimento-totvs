---
content_hash: ddc808611aefab14a962c14fc4177fc5e1c112a848a459474ddf680d96752aaf
fetched_at: '2026-06-29T00:09:11.291345+00:00'
page_id: '403743934'
product: rm
source: tdn-rm
title: DevExpress
type: documentation
url: https://tdn.totvs.com/display/LRM/DevExpress
version: 1
---

-------------------------------  
- 1 Recompilando a DevExpress -  
-------------------------------

1.1 - Verifique se possui o VS 2010 na máquina... a compilação das Dlls de Design dependem de arquivos presentes no VS 2010.  
 . Instale também o VS2010 SDK.  
 . OBS. Não adianta ter uma versão mais nova. Tem que ser o VS2010.

1.2 - Instale a DevExpress somente com os itens que a TOTVS detém a licença. (Normalmente o instalador contém componentes Trial).  
 . Na versão 17 você deve logar com o usuário dono da licença e os componentes dos quais você possui licença serão exibidos.  
 . Selecione os itens: Windows Forms, ASP.NET, WPF, Reporting e Source Code.  
 . Baixar os projetos de localização em <https://localization.devexpress.com/>

Acesso da instalação:  
 [luiz.bilhalva@totvs.com.br](mailto:luiz.bilhalva@totvs.com.br)  
 totvs@123

1.3 - Baixar a versão mais nova do SourceBuilderTool em: <https://www.devexpress.com/Support/Center/Question/Details/A609>

1.4 - Pegar a chave de compilação utilizada pela TOTVS nesta pasta:

- C:\RM\Terceiros\DevX\17.1\Key

Esta é a chave utilizada por nossa equipe para compilar as novas versões das dlls DevX.  
 Deve ser sempre utilizada esta versão, ao invés de gerar um arquivo novo.   
 Para fazer uso da mesma, basta copiá-la para a pasta:  
   
 - C:\Program Files (x86)\DevExpress 17.1\Components\Sources\DevExpress.Key (diretório de instalação da Dev).

Em resumo: Colocar o arquivo StrongKey.snk no diretório Components\Sources\DevExpress.Key (instalação da DevEx).

1.5 - Abrir a SourceBuilderTool e recompilar.

1.6 - Verificar algum erro de compilação.

1.7 - Realizar ckeckout no tfs das dlls da Devexpress localizadas nas pastas:

- $/RM/Atual/Release/Bin  
 - $/RM/Atual/Release/Corpore.Net/Bin  
 - $/RM/Terceiros/DevX/17.1/Bin.DLL (Incluir os arquivos .pdb)  
 - $/RM/Terceiros/DevX/17.1/Bin.Design  
 - $/RM/Terceiros/DevX/17.1/Bin.Localization (Caso precise)

OBS: Esse passo é de extrema importância para o sucesso da substituição das dlls em suas respectivas pastas.

1.7 - Copiar as Dlls utilizadas pelo produto em:

- C:\Program Files (x86)\DevExpress 17.1\Components\Bin\Framework

E atualizar em:

- $/RM/Atual/Release/Bin  
 - $/RM/Terceiros/DevX/17.1/Bin.DLL (Incluir os arquivos .pdb)  
 - $/RM/Atual/Release/Corpore.Net/Bin

1.8 - Atualizar as Dlls de Design em:  
   
 - $/RM/Terceiros/DevX/17.1/Bin.Design

1.9 (Opcional) - Foi criado uma bat [movdll.bat] disponível em:

- $/RM/Terceiros/DevX/17.1/BuildTool

Que agiliza bastante os passos 1.7 e 1.8.

--------------------------------------------  
- 2 Mantendo histórico de builds de versão -  
--------------------------------------------

2.1 - Na pasta /BuildTool existem subpastas onde o resultado da compilação é armazenado. Após o build das Dlls da DevEx pelo SourceBuilderTool,   
 quatro arquivos são gerados na pasta:

- C:\RM\Terceiros\DevX\17.1\BuildTool

São eles:

. build.log => Log do processo de build realizado pela ferramenta SourceBuilderTool. Mostra de forma bem detalhada informações sobre o build das dlls.  
 . build\_erros.log => Log de erros do processo de build realizado pela ferramenta SourceBuilderTool. Mostra de forma bem detalhada quais foram os erros   
 ocorridos durante a geração das dlls.  
 . build\_ToolboxCreate.log => Log da criação dos itens na ToolBox (Caixa de ferramentas) do Visual Studio.  
 . build\_ToolboxRemove.log => Log da remoção dos itens na ToolBox (Caixa de ferramentas) do Visual Studio.

2.2 - Criar uma pasta chamada build\_result\_(n), onde n é o identificador referente ao número de vezes em que o build realizou uma geração válida das dlls (Ex: build\_result\_3).

2.3 - Adicionar os quatro arquivos referidos no item 2.1 na pasta build\_result\_(n)

2.4 - Incluir a pasta build\_result\_(n), juntamente com os arquivos de log no tfs, no caminho:

- $\RM\Terceiros\DevX\17.1\BuildTool

-----------------------------------------------------------------------------------------------------------------------------  
- 3 Recompilando os assemblies de Localização (DEVE SER FEITO SEMPRE QUE MUDAR A VERSÃO MAJOR!! 17.1 para 17.2 por exemplo) -  
-----------------------------------------------------------------------------------------------------------------------------

3.1 - Baixar a versão mais nova do pacote de tradução da versão que está sendo utilizada. Ex. 10.2, 14.1, 17.1 etc. (As traduções só sofrem alterações em nível de Major, 17.1, 17.2).

3.2 - Colocar o arquivo .key no diretório DevExpress.Key da solution.

3.3 - Abrir a solution no Visual Studio e recompilar.

3.4 - Atualizar as pastas de Localização em:  
   
 - $/RM/Atual/Release/Bin  
 - $/RM/Terceiros/DevX/17.1/Bin.Localization  
 - $/RM/Atual/Release/Corpore.Net/Bin

-------------------------------------------------  
- 4 Recriando e Recompilando temas personalizados -  
-------------------------------------------------

4.1 - Dentro do Visual Studio, executar o Skin Editor.

4.2 - Após a abertura do Editor, abra o arquivo [Custom.Skin] de skins localizado em:

- C:/RM/Terceiros/DevX/Skins/17.1/Custom

4.3 - Salve o arquivo, para que a nova versão seja aplicada ao Skin.

4.4 - Altere o arquivo [Custom.Skin] no tfs, localizado em:

$/RM/Terceiros/DevX/Skins/17.1/Custom

4.5 - Gere o assembly [CustomSkins.dll], ele estará localizado em:

- C:/RM/Terceiros/DevX/Skins/17.1/Custom

4.6 - Inclua / Atualize o assembly gerado em:

- $/RM/Atual/Release/Bin  
 - $/RM/Terceiros/DevX/Skins/17.1/Custom

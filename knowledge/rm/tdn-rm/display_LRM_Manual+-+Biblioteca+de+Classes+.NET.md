---
content_hash: 0ab7a80e01bae9480cadf61631dcfcea0fa0703da8965e22c4673d615cc00021
fetched_at: '2026-06-29T00:08:47.278444+00:00'
page_id: '319787288'
product: rm
source: tdn-rm
title: Manual - Biblioteca de Classes .NET
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Biblioteca+de+Classes+.NET
version: 3
---

O contexto de biblioteca de classes .NET permite que seja utilizadas DLLs .NET para leitura dos dados para geração dos registros. Este contexto permite que praticamente qualquer informação seja utilizada para geração do Layout. Pode ser utilizada qualquer versão do Visual Studio ou outras ferramentas de desenvolvimento .NET para geração desta DLL.

![](/download/attachments/319787288/biblioteca_de_classes_net.png?version=1&modificationDate=1512921879000&api=v2)

1Nome do Assembly

Selecione a DLL .NET que será executada para retornar os dados do contexto.

2Classe

Selecione a classe da DLL que será usada para retornar os dados do contexto.

Importante

Algumas regras devem ser seguidas na criação das classes para utilização no contexto do gerador.

1. A classe a ser utilizada deverá ser pública e instânciável, ou seja não pode ser uma classe estática.
2. A classe deverá ter um construtor público, este construtor poderá receber uma classe de parâmetros, desde as propriedades da classe sejam de tipos de valores (string, int, datetime, etc), estes valores serão identificados e preenchidos pelo gerador.
3. A classe deverá ter pelo menos um método público que retorne um enumerado genérico IEnumerable, de uma classe qualquer, esta lista será exposta como uma lista do contexto e poderá ser associada a uma ligação do registro. Todas as propriedades e campos de tipois básicos desta classe serão expostas como campos da lista e poderão ser associados aos campos dos registros. Caso alguma propriedade ou campo for um tipo complexo, o mesmo será exposto como um membro da lista ou uma lista filha caso a propriedades seja um enumerado genérico IEnumerable de uma classe.
4. A DLL deverá ser uma DLL compilada para .NET Core 2 (netcoreapp2), no caso do gerador RM ela deverá ser uma DLL .NET Full utilizando a mesma versão da Framework utilizada pela versão do RM.
5. Para o RM, a classe deverá herdar de RM.Lib.Server.RMSModule e as propriedades disponibilizadas para o gerador deverão utilizar o atributo RM.Lib.ColumnAttribute.

A DLL core deverá estar localizada na mesma pasta do executor Core (onde está localizada a TNF.Gen.Exec.dll) assim como qualquer DLL que ela faça referência. A DLL do gerador RM deverá estar na pasta de instalação da Biblioteca (RM.NET).

#### Exemplo

O exemplo a seguir expõe os dados dos processos em execução no sistema para o gerador de saídas. Como parâmetro ele pode receber o nome da máquina que deseja listar os processos. O método ListaProcessos() irá ser executado pelo gerador e as propriedades das classes TestProcInfo e TestThreadInfo poderão ser utilizadas para gerar os registros do Layout.

Código

```
using System;
using System.Collections.Generic;
using System.Diagnostics;
namespace RM.Gen.Test
{
  /// 
  /// Classe de teste para uso no gerador de saídas
  ///   
  public class TestClass
  {
    private TestClassParam Parameters;
    /// 
    /// Cria uma instância da classe
    /// 
    /// Nome da máquina para listagem dos processos
    public TestClass(TestClassParam parameters)
    {
      this.Parameters = parameters;
    }
    /// 
    /// Lista os processos em execução na máquina
    /// 
    /// 
    public List ListaProcessos()
    {
      List lista = new List();
      // carrega os processo em execução na máquina...
      Process[] procs;
      if (this.Parameters != null && !string.IsNullOrEmpty(this.Parameters.MachineName))
        procs = Process.GetProcesses(this.Parameters.MachineName);
      else
        procs = Process.GetProcesses();
      // carrega as classes de resultado...
      foreach (Process proc in procs)
        lista.Add(new TestProcInfo(proc));
      return lista;
    }
  }
  /// 
  /// Parâmetros informados pelo gerador
  /// 
  public class TestClassParam
  {
    public string MachineName { get; set; }
  }
  /// 
  /// Dados do processo do sistema
  /// 
  public class TestProcInfo
  {
    public TestProcInfo(Process proc)
    {
      this.Id = proc.Id;
      this.Titulo = proc.MainWindowTitle;
      this.MemoriaMax = proc.PeakWorkingSet64;
      this.MemoriaEmUso = proc.WorkingSet64;
      try
      {
        this.HoraInicio = proc.StartTime;
      }
      catch
      {
      }
      // carrega a lista de threads...
      this.Threads = new List();
      foreach (ProcessThread procThread in proc.Threads)
        this.Threads.Add(new TestThreadInfo(procThread));
    }
    public int Id { get; private set; }
    public string Titulo { get; private set; }
    public long MemoriaMax { get; private set; }
    public long MemoriaEmUso { get; private set; }
    public DateTime HoraInicio { get; private set; }
    public List Threads { get; private set; }
  }
  /// 
  /// Dados da Thread do Processo
  /// 
  public class TestThreadInfo
  {
    public TestThreadInfo(ProcessThread procThread)
    {
      this.Id = procThread.Id;
      if (procThread.ThreadState == ThreadState.Running)
      {
        try
        {
          this.Processamento = procThread.UserProcessorTime;
          this.HoraInicio = procThread.StartTime;
        }
        catch
        {
        }
      }
    }
    public int Id { get; private set; }
    public DateTime HoraInicio { get; private set; }
    public TimeSpan Processamento { get; private set; }
  }
}
```
